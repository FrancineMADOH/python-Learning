from django.urls import  path, include
from . import views

urlpatterns = [
    path('', views.landing_page,name='home'),
    path('view/<int:objective_id>/', views.view_objective,name='objective-details')
]
