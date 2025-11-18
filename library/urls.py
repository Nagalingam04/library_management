from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.base, name='base'),
    path('home', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit'),
    path('delete/<int:book_id>/', views.delete_book, name='delete'),
]
