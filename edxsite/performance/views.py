from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from performance.models import problem, week_problem
from django.template import loader


def index(request):
    return render(request, 'performance/index.html')


def week_list(request):
    # return a list of week number we current have in the database
    week_number = week_problem.objects.only('set_id').distinct('set_id')
    context = {'week_list': week_number}
    return render(request, 'performance/week_list.html', context)


def problem_list(request, week_id):
    # return a list of problem number for a specific week
    problem_number = week_problem.objects.filter(set_id='Week' + week_id).distinct('problem_id')
    problem_number_sort = []
    for p in problem_number:
        problem_number_sort.append(int(p))
    problem_number_sort.sort()
    context = {'problem_list': problem_number_sort}
    return render(request, 'performance/problem_list.html', context)