import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book.models import Book
from book.serializers import BookSerializer


@api_view(['GET'])
def greet(request):
    if request.method == 'GET':
        return Response("Welcome in book-api.")


@api_view(['GET'])
def get_all_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_book(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def insert_book(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['PUT'])
def update_book(request, pk):
    if request.method == 'PUT':
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def delete_book(request, pk):
    if request.method == 'DELETE':
        book = Book.objects.get(id=pk)
        book.delete()
        return Response('Deleted')
