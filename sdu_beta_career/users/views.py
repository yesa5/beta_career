from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from ..access_control.config import Policy
from .forms import ProfileEditForm
from .models import Profile

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserListView(LoginRequiredMixin, ListView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_list_view = UserListView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class ProfileDetailView(DetailView):
    template_name = 'users/profile_details.html'
    model = Profile

    def dispatch(self, request, *args, **kwargs):
        if(self.request.user.is_anonymous
                or not self.request.user.access_control.can_read(Policy.PROFILE_OWN)
                or not self.request.user.access_control.can_write(Policy.PROFILE_OWN)):

            return redirect('users:profile')

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs.get('pk'))
        context['profile'] = profile
        context['form'] = ProfileEditForm(instance=profile)
        return context

    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=self.kwargs.get('pk'))
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            context = super().get_context_data(**kwargs)
            context['profile'] = profile
            context['form'] = ProfileEditForm(instance=profile)
            return self.render_to_response(context=context)
        else:
            context = super().get_context_data(**kwargs)
            context['profile'] = profile
            context['form'] = ProfileEditForm(instance=profile)
            return self.render_to_response(context=context)


class ProfileListView(ListView):
    context_object_name = 'profiles'
    queryset = Profile.objects.all()
    template_name = 'users/profile_lists.html'
