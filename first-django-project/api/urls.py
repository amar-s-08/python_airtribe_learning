from django.urls import path
from .views import add_two_numbers, hello

urlpatterns = [
    path("hello/",hello),
    path("addTwoNumbers/",add_two_numbers)
]