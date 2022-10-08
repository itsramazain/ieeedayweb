from django.shortcuts import render
from django.views import generic


class HomePgae(generic.TemplateView):
    template_name='ieeeday.html'

class Thanks(generic.TemplateView):
    template_name='thanks.html'

class Logg(generic.TemplateView):
    template_name='logg.html'
