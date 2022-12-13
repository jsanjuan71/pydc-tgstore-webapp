from django.urls import path

from . import views

urlpatterns = [
    path("", views.home ), #store/
    path("users", views.users), #store/users
    path("products", views.products)
]