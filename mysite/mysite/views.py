# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main.html')


@login_required
def members(request):
    return HttpResponse('<p>only members can see.</p>')





