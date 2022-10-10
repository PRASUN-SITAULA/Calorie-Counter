from django.urls import path
from . import views

urlpatterns =[
    path("", views.home, name="home"),
    path("add/", views.add_food, name="add"),
    path("update/<int:pk>/", views.update_food, name="update"),
    path("details/", views.details, name="details"),
    path("delete/<int:pk>/", views.delete_food, name="delete"),
    path("login/", views.loginpage, name="loginpage"),
    path("logout/", views.logoutpage, name="logout"),
]