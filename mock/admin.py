from django.contrib import admin
from .models import Choice, Question, Result, Test, ResultChoice
# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Test)
admin.site.register(ResultChoice)