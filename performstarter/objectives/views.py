from django.shortcuts import render


from .models import  Objective


def landing_page(request):
    objectives = Objective.objects.all()
    # firebase security rules how they apply on firebase real time and on firestore db

    return render(request, 'objectives/home.html', {'objectives': objectives} )
#manage.py migrate --run-syncdb

def view_objective(request,objective_id):
    objective = Objective.objects.get(objective_id = objective_id)

    return render(request, 'objectives/detail_objective.html' ,{'objective':objective})