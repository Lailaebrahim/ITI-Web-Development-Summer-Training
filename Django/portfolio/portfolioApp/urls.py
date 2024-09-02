from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name="home"),
    path('projects',  ProjectsListView.as_view(), name="projects"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name="project"),
    path('contact', contact, name="contact"), 
    path('contributer/<int:pk>/',
         ContributerDetailView.as_view(), name="contributor"),
    path("project/create", ProjectCreateView.as_view(), name="createProject"),
    path("project/<int:project_id>/delete/", ProjectDeleteView, name="deleteProject"),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name="updateProject"),
    path("contibuter/create/", ContributerCreateView.as_view(), name="createContributer"),
    path("contributer/<int:pk>/update/", ContributerUpdateView.as_view(), name="updateContributer"),
    path("contributer/<int:contributer_id>/delete/", ContributerDeleteView, name="deleteContributer"),
    path("contributers/", ContributerListView.as_view(), name="contributers"),
    path("contribution/<int:project_id>/create/",
         ContributionCreateView.as_view(), name="createContribution"),
    path("contributer/<int:contributer_id>/addTechnology/",
         ContributerTechnologyCreateView.as_view(), name="addContributerTechnology"),
    path('technology/create', TechnologyCreateView.as_view(), name="createTechnology"),
    path('technology/<int:technology_id>/delete',
         TechnologyDeleteView, name="deleteTechnology"),
    path('technology/<int:pk>/update',
         TechnologyUpdateView.as_view(), name="updateTechnology"),
]
