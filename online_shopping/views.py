from django.shortcuts import render, redirect


def BASE(request):

    return render(request, 'main/base.html')


def home(request):

    return render(request,'main/index.html')