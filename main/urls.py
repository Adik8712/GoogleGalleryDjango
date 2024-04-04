from django.urls import path
from .views import index, Add_Post, SingUpUser, logoutUser, SingInUser, posts, ContactView, AddCategory, AnimeView

urlpatterns = [
    path('', index),
    path('anime/', AnimeView),
    path("posts/", posts),
    path("add/", Add_Post),
    path("category/", AddCategory),
    path("singup/", SingUpUser),
    path("logout/", logoutUser),
    path("login/", SingInUser),
    path("contact/", ContactView),
]
