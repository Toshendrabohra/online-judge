from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("", views.index,name="home"),
    path("leaderboard", views.leaderboard,name="leaderboard"),
    path("problem_page/<int:pid>",views.problem_page,name="problem_page"),
    path("submit/<int:pid>",views.submit,name="submit"),
    path('',include('users.urls')),
]