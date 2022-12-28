from django.urls import path
from questions import views

urlpatterns=[
    path('findQuest', views.questApi)

]