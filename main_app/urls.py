from django.urls import path
from . import views

urlpatterns = [
    # path for the home page.
    path('', views.Home.as_view(), name = "home"),
    # path for motorcycle company list page
    path('motorcycle_co_list/', views.Motorcycle_Co_List.as_view(), name = "motorcycle_co_list"),
    #path to add motorcycle company to motorcycle list
    path('motorcycle_co_list/new', views.Motorcycle_Co_Create.as_view(), name = "motorcycle_co_create"),
    # path for details page of the company, motorcycle models will go here
    path('motorcycle_co_list/<int:pk>/', views.Motorcycle_Co_Details.as_view(), name = "motorcycle_co_details"),
    # path to update motorcycle company
    path('motorcycle_co_list/<int:pk>/update', views. Motorcycle_Co_Update.as_view(), name = "motorcycle_co_update"),
    # path for deleting motorcycle company
    path('motorcycle_co_list/<int:pk>/delete', views.Motorcycle_Co_Delete.as_view(), name = "motorcycle_co_delete"),
]