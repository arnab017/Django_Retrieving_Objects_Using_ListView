from django.shortcuts import render
from django.views.generic import ListView
from app.models import *
# Create your views here.

class Trainer_list(ListView):
    #-----model is capable of writing the query to get all the objects for given model
    model = Trainer
    #-----template_name is used to specify in which template it will render the List of Objects
    template_name = 'Trainer_list.html'
    #-----context_object_name is the name of the context to be sent to template 
    context_object_name = 'tl'
    #-----query set is used if user wants custom query set to execute
    # queryset = Trainer.objects.filter(tsubject='Python')
    #-----ordering is used to show in which order you want to display the objects
    ordering = ['tname']
    