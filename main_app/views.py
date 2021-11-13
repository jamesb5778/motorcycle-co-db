from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
#view for the homepage
class Home(TemplateView):
    template_name = "home.html"

#view for the motorcycle company list
class Motorcycle_Co_List(View):
    def get(self, request):
        return HttpResponse("List of Motorcycle Companies")