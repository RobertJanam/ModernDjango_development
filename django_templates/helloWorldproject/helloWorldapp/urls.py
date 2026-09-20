from django.urls import path
from . import views

urlpatterns = [
    path('test/<name>/', views.test, name='test'),
    path('index/<name>/', views.index, name='index'),
    path('marks/', views.marks, name='marks'),
]