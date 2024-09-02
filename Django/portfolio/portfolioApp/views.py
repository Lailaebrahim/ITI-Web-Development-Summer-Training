from django.shortcuts import render, get_object_or_404, resolve_url
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Project, Contributer, ContributorProjectContribution, ContributerTechnology, Technology
from .forms import ProjectForm, ContributerForm,  ContributionForm, ContributerTechnologyForm, TechnologyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
# Create your views here.


def home(request):
    developer = {
        "name": "Laila Ebrahim",
        "age": 24,
        "position": "Full Stack Developer",
        "bio": "I'm Laila Ebrahim, a passionate Python web developer with a focus on creating efficient, scalable, and user-friendly web applications.",
        "years": "1",
    }
    return render(request, 'portfolioApp/home.html', context={"dev": developer})


def contact(request):
    return render(request, 'portfolioApp/contact.html')


class ProjectsListView(ListView):
    model = Project
    template_name = 'portfolioApp/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.prefetch_related(
            Prefetch(
                'contributor_contributions',
                queryset=ContributorProjectContribution.objects.select_related(
                    'contributor'),
                to_attr='prefetched_contributions'
            ),
        )


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolioApp/project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contributers'] = ContributorProjectContribution.objects.filter(
            project=self.object
        )
        return context


class ContributerDetailView(DetailView):
    model = Contributer
    template_name = 'portfolioApp/contributor.html'
    context_object_name = 'contributor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contributions'] = ContributorProjectContribution.objects.filter(
            contributor=self.object
        )
        context['technologies'] = ContributerTechnology.objects.filter(
            contributer=self.object)
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "portfolioApp/create_project.html"
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.portfolio_user = self.request.user.portfolio_user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolioApp/update_project.html'
    success_url = reverse_lazy('projects')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.portfolio_user != request.user.portfolio_user:
            raise PermissionDenied("You are not allowed !!")
        return super().dispatch(request, *args, **kwargs)

@login_required
def ProjectDeleteView(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if (request.user.portfolio_user != project.portfolio_user):
        raise PermissionDenied("You are not allowed !!")
    else:
        project.delete()
    return HttpResponseRedirect(reverse_lazy('projects'))


class ContributerCreateView(LoginRequiredMixin, CreateView):
    model = Contributer
    form_class = ContributerForm
    template_name = "portfolioApp/create_contributer.html"
    success_url = reverse_lazy('contributers')

    def form_valid(self, form):
        form.instance.portfolio_user = self.request.user.portfolio_user
        return super().form_valid(form)


class ContributerUpdateView(LoginRequiredMixin, UpdateView):
    model = Contributer
    form_class = ContributerForm
    template_name = 'portfolioApp/update_contributer.html'
    success_url = reverse_lazy('contributers')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.portfolio_user != request.user.portfolio_user:
            raise PermissionDenied("You are not allowed !!")
        return super().dispatch(request, *args, **kwargs)


class ContributerListView(ListView):
    model = Contributer
    template_name = 'portfolioApp/contributers.html'
    context_object_name = 'contributers'

    def get_queryset(self):
        return Contributer.objects.prefetch_related(
            Prefetch(
                'project_contributions',
                queryset=ContributorProjectContribution.objects.select_related(
                    'project'),
                to_attr='contributions'
            ),
            Prefetch(
                'contributer_technologies',
                queryset=ContributerTechnology.objects.select_related(
                    'technology'),
                to_attr='technologies'
            )
        )


@login_required
def ContributerDeleteView(request, contributer_id):
    contributer = get_object_or_404(Contributer, id=contributer_id)
    if (request.user.portfolio_user != contributer.portfolio_user):
        raise PermissionDenied("You are not allowed !!")
    else:
        contributer.delete()
    return HttpResponseRedirect(reverse_lazy('projects'))


class ContributionCreateView(LoginRequiredMixin, CreateView):
    model = ContributorProjectContribution
    form_class = ContributionForm
    template_name = "portfolioApp/create_contribution.html"
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        project_id = self.kwargs.get('project_id')
        form.instance.project = get_object_or_404(Project, id=project_id)
        return super().form_valid(form)


class ContributerTechnologyCreateView(LoginRequiredMixin, CreateView):
    model = ContributerTechnology
    form_class = ContributerTechnologyForm
    template_name = "portfolioApp/add_technology.html"
    success_url = reverse_lazy('contributers')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        contributer_id = self.kwargs.get('contributer_id')
        kwargs['contributer'] = get_object_or_404(
            Contributer, id=contributer_id)
        return kwargs

    def form_valid(self, form):
        form.instance.contributer = form.contributer
        return super().form_valid(form)


class TechnologyCreateView(LoginRequiredMixin, CreateView):
    model = Technology
    form_class = TechnologyForm
    template_name = "portfolioApp/create_technology.html"
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.portfolio_user = self.request.user.portfolio_user
        return super().form_valid(form)
    
@login_required
def TechnologyDeleteView(request, technology_id):
    technology = get_object_or_404(Technology, id=technology_id)
    if (request.user.portfolio_user != technology.portfolio_user):
        raise PermissionDenied("You are not allowed !!")
    else:
        technology.delete()
    return HttpResponseRedirect(reverse_lazy('projects'))

class TechnologyUpdateView(LoginRequiredMixin, UpdateView):
    model = Technology
    form_class = TechnologyForm
    template_name = 'portfolioApp/update_technology.html'
    success_url = reverse_lazy('projects')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.portfolio_user != request.user.portfolio_user:
            raise PermissionDenied("You are not allowed !!")
        return super().dispatch(request, *args, **kwargs)
