from django.urls import path
from . import views

urlpatterns = [
    # since django resolver sends requests and path parameters to a callable function and we are using a class in our view, we add as_view() class method
    path('name/', views.MyView.as_view(), name="name"),
]
