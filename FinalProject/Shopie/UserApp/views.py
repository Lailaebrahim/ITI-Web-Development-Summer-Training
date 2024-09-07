from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, UserUpdateForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import ShopieUser
from django.contrib.auth.models import User
from django.urls import reverse_lazy


@login_required
def LogOutView(request):
    logout(request)


def SignUpView(request):
    if request.method == 'GET':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'registration/signup.html', {'form': form})


class UserAccountView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'UserApp/userAccount.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopieuser'] = ShopieUser.objects.get(user=self.object.id)
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = ShopieUser
    template_name = 'UserApp/userUpdate.html'
    form_class = UserUpdateForm
    context_object_name = 'shopieuser'

    def get_object(self, queryset=None):
        return self.request.user.shopieuser

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('userAccount', kwargs={'pk': self.object.user.id})


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "userApp/userDelete.html"
    success_url = reverse_lazy('home')
