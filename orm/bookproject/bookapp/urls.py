from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:id>/', views.book, name='book'),
    path('test/', views.test, name='test'),
    path('books/', views.books, name="books"),
    path('getbook/', views.getbook, name='getbook'),
    path('addbook/', views.addbook, name='addbook')
]