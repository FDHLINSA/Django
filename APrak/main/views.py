from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')
def main(request):
    return render(request, 'dashboard/index.html')
