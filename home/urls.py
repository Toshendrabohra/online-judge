from django.contrib import admin
from django.urls import path, include, re_path
from home import views
urlpatterns = [
    path("", views.index,name="home"),
    path("leaderboard", views.leaderboard,name="leaderboard"),
    re_path(r'^problem_page/(?P<pid>[0-9a-f\-]{32,})$',views.problem_page,name="problem_page"),
    re_path(r'^submit/(?P<pid>[0-9a-f\-]{32,})',views.submit,name="submit"),
    path('',include('users.urls')),
]