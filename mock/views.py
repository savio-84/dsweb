from django.shortcuts import render
from django.views import generic, View
from .models import Test, Result, Question, Choice, ResultChoice
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model, authenticate

# Create your views here.
# @user_passes_test(login_url='/login/')
class Dashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mock/dashboard.html', {"user": request.user})

def landingPage(request):
    question = Question.objects.all()
    return render(request, 'mock/landing.html', { "questions": question })

class MyQuestions(View):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.filter(test__owner = request.user)
        return render(request, 'mock/myquestions.html', {"questions": questions})

class EmailBackend(ModelBackend):
    def authenticate(request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mock/login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = EmailBackend.authenticate(
            request, username=email, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect(reverse("dashboard"))
            return render(request, 'mock/dashboard.html', {'user': request.user})
        else:
            erro = 'Email e senha inválidas!'

            return render(request, 'mock/login.html', {'erro': erro})
            
class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mock/register.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        # posteriormente verificar se já existe conta com o msm email,cpf.
        email = request.POST.get("email")
        password = request.POST.get("password")
        if name and email and password:
            user = User.objects.create_user(
                username=name, password=password, email=email)
            # return HttpResponseRedirect(reverse("login"))
            return render(request, 'mock/login.html')
        else:
            erro = 'Informe corretamente os parâmetros necessários!'

            return render(request, 'mock/register.html', {'erro': erro})

def result(request, test_id):
    test = Test.objects.get(pk = test_id)
    questions = Question.objects.filter(test__id = test.id)
    totalValue = 0
    for question in questions:
        totalValue += question.value

    result = Result.objects.create(test = test, student = test.owner, value = totalValue, result = 0)

    for question in questions:
        choice = Choice.objects.get(pk=request.POST.get(str(question.id))[0])
        
        rc = ResultChoice.objects.create(choice = choice, result = result)
        rc.save()

        choice.marked = True
        if choice.is_correct == True:
            result.result = result.result + choice.value

    result.save()

    resultChoices = ResultChoice.objects.filter(result = result)

    response = {
        'result': result,
        'choiceResults': resultChoices
    }
    return render(request, 'mock/result.html', response)

class TestIndexView(generic.ListView):
    template_name = 'mock/index.html'
    context_object_name = 'tests_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Test.objects.all

class TestDetailView(generic.DetailView):
    model = Test
    template_name = 'mock/test.html'

class MyTests(View):
    def get(self, request, *args, **kwargs):
        tests = Test.objects.filter(owner__id = request.user.id)
        return render(request, 'mock/mytests.html', {'tests': tests})
