from .views import BookListView,BookDetailView,AuthorDetailView,AuthorListView,BookUtilAPIView
from django.urls import path

urlpatterns = [
    path('',BookListView.as_view(),name='books'),
    path('books/<slug>',BookDetailView.as_view(),name='book_detail'),
    path('books/',BookUtilAPIView.as_view(),name='book_create'),
    path('authors',AuthorListView.as_view(),name='authors'),
    path('authors/<slug>',AuthorDetailView.as_view(),name='author_detail'),
]