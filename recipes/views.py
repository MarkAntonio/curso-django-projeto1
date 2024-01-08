from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("New home")


def contato(request):
    return HttpResponse("New contato")


def sobre(request):
    return HttpResponse("Sobre")

