from django.contrib import admin
from django.urls import path
from data import views

urlpatterns = [
    path("", views.index, name='data'),

    path("event", views.all_events, name='list-Admission'),
    path("event2", views.all_events2, name='list-Admission2'),
    path("Student", views.Student, name='Student'), 
]