from django.urls import path 
from books import views 
 
urlpatterns = [ 
    path('api/books', views.BookListView.as_view()),
    path('api/books/<int:pk>', views.BookDetailView.as_view()),
    path('api/books/published', views.BookSpecialView.as_view())
]