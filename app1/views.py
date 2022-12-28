from django.shortcuts import render

from django.http import HttpResponse
def Hemanth(request):
    return HttpResponse ('<h1>Hemanth loves Shashikala</h1>')

def Naveen(request):
    return HttpResponse ('<h1>This string is for Naveen</h1>')