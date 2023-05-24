from django.shortcuts import render
from django.http import HttpResponse
#lets you return http response where you can pass in a string

def show_recipe(request):
    return HttpResponse("This view is working")
