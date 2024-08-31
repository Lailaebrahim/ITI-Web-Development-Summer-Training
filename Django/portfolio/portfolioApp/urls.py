from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name="home"),
    #path('skills', skills, name="skills")
    path('projects',  ProjectsListView.as_view(), name="projects"),
    path('contact', contact, name="contact"), 
    path('contributor/<int:pk>/',
         ContributerDetailView.as_view(), name="contributor"),
    path("project/create", ProjectCreateView.as_view(), name="createProject"),
    path("project/<int:project_id>/delete/", ProjectDeleteView, name="deleteProject"),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name="updateProject"),
    path("contibuter/create/", ContributerCreateView.as_view(), name="createContributer"),
    path("contributer/<int:pk>/update/", ContributerUpdateView.as_view(), name="updateContributer"),
    path("contributer/<int:contributer_id>/delete/", ContributerDeleteView, name="deleteContributer"),
    path("contributers/", ContributerListView.as_view(), name="contributers")
]
