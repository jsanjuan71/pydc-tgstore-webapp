from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home" ),
    path("products", views.products, name="catalog"),
    path("cart", views.cart, name="cart"),
    path("account", views.account, name="account")
]