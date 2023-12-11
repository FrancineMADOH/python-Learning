from django.shortcuts import render

from . import models


def landing_page(request):

    return render(request, 'objectives/home.html', {})

def view_objective(request):

    return render(request, 'objectives/objective.html' ,{})