from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
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
        name = self.request.GET.get("name")
        if name != None:
            context["motorcycle_company"] = Motorcycle_Company.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["motorcycle_company"] = Motorcycle_Company.objects.all()
            context["header"] = "Motorcycle Companies"
        return context
    
# view to create/add a motorcycle company to motorcycle_co_list
class Motorcycle_Co_Create(CreateView):
    model = Motorcycle_Company
    fields = ['name', 'image', 'founded', 'description']
    template_name = "motorcycle_co_create.html"
    success_url = "/motorcycle_co_list/"

# view for Motorcycle company details
class Motorcycle_Co_Details(DetailView):
    model = Motorcycle_Company
    template_name = "motorcycle_co_details.html"

# view for Motorcycle company update
class Motorcycle_Co_Update(UpdateView):
    model = Motorcycle_Company
    fields = ['name', 'image', 'founded', 'description']
    template_name = "motorcycle_co_update.html"
    success_url = "/motorcycle_co_list/"