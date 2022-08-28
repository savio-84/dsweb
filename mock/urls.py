from django.urls import path
from . import views

app_name = 'mock'
urlpatterns = [
    path('', views.landingPage, name="LandingPage"),
    path('login/', views.Login.as_view(), name="login"),
    path('register/', views.Register.as_view(), name="register"),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('tests/', views.TestIndexView.as_view(), name="TestsList"),
    path('test/<int:pk>/', views.TestDetailView.as_view(), name="TestDetail"),
    path('test/<int:test_id>/result', views.result, name="TestResult"),
    path('my-questions/', views.MyQuestions.as_view(), name="MyQuestions"),
    path('my-tests/', views.MyTests.as_view(), name="MyTests")
]