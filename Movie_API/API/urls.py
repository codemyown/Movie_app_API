from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   path("",views.index),
   path("contact",views.contact,name = 'contact '),
   path("ContactAPI",views.api_contact,name = 'api_contact'),
   path("gallaryAPI",views.gallaryAPI,name = "gallaryAPI"),
   path("movieAPI",views.movieAPI,name = "movieAPI")
]
