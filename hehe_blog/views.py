from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
# Create your views here.


def main(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')

def now_date(request):
    if request.method == 'GET':
        return HttpResponse(f'Now: {datetime.now()}')

def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
