from django.urls import path
from books import views
urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.book_list, name='book_list'),
    path('book/book_detail/<int:pk>', views.book_detail, name='book_detail'),
    path('book/book_create/', views.book_create, name='book_create'),
    path('book/book_update/<int:pk>/', views.book_update, name='book_update'),
    path('book/book_delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]


