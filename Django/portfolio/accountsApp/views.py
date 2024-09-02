from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, PortfolioUserForm, UserForm, UpdateAccountForm
from .models import PortfolioUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.db.models import Prefetch  # Add this line
from portfolioApp.models import Project, Contributer, Technology, ContributorProjectContribution, ContributerTechnology

# Create your views here.
def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', context={"form": form})


@login_required
def LogOutView(request):
    logout(request)


class AccountView(LoginRequiredMixin, DetailView):
    model = PortfolioUser
    template_name = 'accountsApp/account.html'
    context_object_name = 'portfoliouser'


@login_required
def AccountDeleteView(request):
    user = request.user
    portfoliouser = request.user.portfolio_user
    portfoliouser.delete()
    user.delete()
    return HttpResponseRedirect(reverse_lazy('projects'))


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accountsApp/accountUpdate.html'
    form_class = UpdateAccountForm
    success_url = reverse_lazy('projects')

    def get_object(self):
        return self.request.user
    
    def get_form_instance(self):
        return self.request.user

    def form_valid(self, form):
        form.save(commit=True)
        return super().form_valid(form)
    

class UserProjectsView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'portfolioApp/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(portfolio_user=self.request.user.portfolio_user)

class UserContributersView(LoginRequiredMixin, ListView):
    model = Contributer
    template_name = 'portfolioApp/contributers.html'
    context_object_name = 'contributers'

    def get_queryset(self):
        return Contributer.objects.filter(portfolio_user=self.request.user.portfolio_user).prefetch_related(
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

class UserTechnologiesView(LoginRequiredMixin, ListView):
    model = Technology
    template_name = 'portfolioApp/technologies.html'
    context_object_name = 'technologies'

    def get_queryset(self):
        return self.request.user.portfolio_user.technologies