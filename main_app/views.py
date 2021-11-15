from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Motorcycle_Company

# Create your views here.
#view for the homepage
class Home(TemplateView):
    template_name = "home.html"

#view for the motorcycle company list
class Motorcycle_Co_List(TemplateView):
    template_name = "motorcycle_co_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["motorcycle_company"] = Motorcycle_Company.objects.all()
        return context