from django.shortcuts import render
from django.http import HttpResponse

def odd_or_even(request, number):
    if number%2==0:
        i = "odd"
    else:
        i = "even"
    return HttpResponse(f"<h1>{number} is {i}</h1>")
