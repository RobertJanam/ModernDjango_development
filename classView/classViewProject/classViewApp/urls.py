from django.urls import path
from . import views

urlpatterns = [
    # since django resolver sends requests and path parameters to a callable function and we are using a class in our view, we add as_view() class method
    path('name/', views.MyView.as_view(), name="name"),
    path('name/<name>', views.IndexView.as_view(), name='name'),
    path('getbook/', views.addbook, name='addbook'),
    path('newbook/', views.CreateBookView.as_view(), name='newbook'),
    path('getbooks/', views.displaybook, name='getbooks'),
]
