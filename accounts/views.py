from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    template_name = "accounts/login.html"
    args = {}
    args["title_here"] = "Login"
    return render(request, template_name,args)
