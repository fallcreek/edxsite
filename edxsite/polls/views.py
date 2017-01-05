from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import problem


def index(request):
    output = ''
    for entry in problem.objects:
        output = str(entry.week)

    return HttpResponse(output)


