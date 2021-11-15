from django.urls import path
from . import views

urlpatterns = [
    # path for login
    # path for the home page.
    path('', views.Home.as_view(), name = "home"),
    # path for motorcycle company list page
    path('motorcycle_co_list/', views.Motorcycle_Co_List.as_view(), name = "motorcycle_co_list"),
    # path for single motorcycle company. List all the motorcycle models
    # path for single model of motorcycle
    
    
]