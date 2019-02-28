from django.urls import path
from crudbook import views

app_name = 'crudbook'
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/update/', views.book_update, name='book_update'),
]
