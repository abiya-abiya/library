from django.urls import path
from books import views
urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.book_list, name='book_list'),
    path('book/book_detail/<int:pk>', views.book_detail, name='book_detail'),
    path('book/book_create/', views.book_create, name='book_create'),
]


