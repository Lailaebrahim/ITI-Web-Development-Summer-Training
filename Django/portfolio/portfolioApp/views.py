from django.shortcuts import render, get_object_or_404, resolve_url
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Project, Contributer
from .forms import ProjectForm, ContributerForm
"""is_superuser"""

# Create your views here.
def home(request):
    developer = {
        "name": "Laila Ebrahim",
        "age": 24,
        "position": "Full Stack Developer", 
        "bio": "I'm Laila Ebrahim, a passionate Python web developer with a focus on creating efficient, scalable, and user-friendly web applications.",
        "years" :"1",
    }
    return render(request, 'portfolioApp/home.html', context={"dev": developer})

def contact(request):
    return render(request, 'portfolioApp/contact.html')

class ProjectsListView(ListView):
    model = Project
    template_name = 'portfolioApp/projects.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        return Project.objects.all()

"""def skills(request):
    return render(request, 'portfolioApp/skills.html')"""

class ContributerDetailView(DetailView):
    model = Contributer
    template_name = 'portfolioApp/contributor.html'
    context_object_name = 'contributor'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "portfolioApp/create_project.html"
    success_url = reverse_lazy('projects')
    
class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolioApp/update_project.html'
    success_url = reverse_lazy('projects')


def ProjectDeleteView(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return HttpResponseRedirect(reverse_lazy('projects'))

class ContributerCreateView(CreateView):
    model = Contributer
    form_class = ContributerForm
    template_name = "portfolioApp/create_contributer.html"
    success_url = reverse_lazy('contributers')
    
class ContributerUpdateView(UpdateView):
    model = Contributer
    form_class = ContributerForm
    template_name = 'portfolioApp/update_contributer.html'
    success_url = reverse_lazy('contributers')
    
class ContributerListView(ListView):
    model = Contributer
    template_name = 'portfolioApp/contributers.html'
    context_object_name = 'contributers'
    
    def get_queryset(self):
        return Contributer.objects.all()

def ContributerDeleteView(request, contributer_id):
    contributer = get_object_or_404(Contributer, id=contributer_id)
    contributer.delete()
    return HttpResponseRedirect(reverse_lazy('projects'))
