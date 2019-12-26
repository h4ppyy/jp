import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.conf import settings


def index(request):
    context = {}
    return render(request, 'post/index.html', context)
