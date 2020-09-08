from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView,ListAPIView,CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from .serializers import BookSerializer,AuthorSerializer,BookUtilSerializer
from .models import Book,Author


class BookListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (AllowAny,)
    

class BookDetailView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'slug'

class BookUtilAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()
    serializer_class = BookUtilSerializer


class AuthorListView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (AllowAny,)
    
    
class AuthorDetailView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'slug'

# class ddfdjk

    

