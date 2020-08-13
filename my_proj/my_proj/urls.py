"""my_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from book.views import get_all_books

from book.views import insert_book

from book.views import get_book

from book.views import update_book , delete_book, greet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', greet),
    path('book/', greet),
    path('book-all', get_all_books),
    path('book/<str:pk>', get_book),
    path('book-insert', insert_book),
    path('book-update/<str:pk>', update_book),
    path('book-delete/<str:pk>', delete_book)
]
