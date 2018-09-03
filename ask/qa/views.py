from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def test_ok(request, *args, **kwargs):
    return HttpResponse('OK')