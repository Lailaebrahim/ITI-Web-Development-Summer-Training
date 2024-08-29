from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('skills', views.skills, name="skills"),
    path('projects', views.projects, name="projects"),
    path('contact', views.contact, name="contact"), 
    path('contributor/<int:contributor_id>/',
         views.contributor, name="contributor"),
]
