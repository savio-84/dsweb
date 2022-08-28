from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=250)
    value = models.FloatField()
    def __str__(self) -> str:
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)
    value = models.FloatField()

    def __str__(self) -> str:
        return self.choice_text
    
class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField()
    result = models.FloatField()

class ResultChoice(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)