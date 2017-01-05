from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from performance.models import problem
from django.template import loader

def index(request):
    problem_list = problem.objects
    context = {'problem_list': problem_list}
    return render(request, 'performance/index.html', context)


def week_detail(request, week_id):
    response = "You're looking at the results of week %s."
    return HttpResponse(response % week_id)