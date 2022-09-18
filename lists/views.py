from django.shortcuts import render
from django.http import HttpResponse

def home_page(variable):
    return HttpResponse('<html><title>To-Do Lists</title></html>')
