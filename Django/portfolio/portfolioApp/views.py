from django.shortcuts import render, get_object_or_404
from .models import Project, Contributer

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

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolioApp/projects.html', context={"projects": projects})

def skills(request):
    return render(request, 'portfolioApp/skills.html')


def contributor(request, contributor_id):
    contributor = get_object_or_404(Contributer, id=contributor_id)
    return render(request, 'portfolioApp/contributor.html', context={"contributor": contributor})

