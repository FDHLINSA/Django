from django.shortcuts import render
from .models import Book

# Create your views here.
def login(request):
    return render(request, 'login/login.html')
def main(request):
    books = Book.objects.all()
    return render(request, 'dashboard/index.html', {'books' : books})
  