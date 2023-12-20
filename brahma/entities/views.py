from typing import Any
from django.conf import settings
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CommunityForm, RegisterForm, UserProfileForm
from .models import User, Community, CommunityMembership, Location, OtherEntity


class IndexView(generic.TemplateView):
    template_name = "brahma/index.html"


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "entities/user_form.html"
    success_url = "/"


class CommunityCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CommunityForm
    template_name = "entities/community_form.html"

    def get_success_url(self) -> str:
        comm_obj = self.get_form().instance
        CommunityMembership.objects.create(community=comm_obj, member=self.request.user, membership_type="admin")
        
        return reverse('community', args=[comm_obj.slug])


class EntityCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CommunityForm
    template_name = "entities/community_form.html"

    def get_success_url(self) -> str:
        comm_obj = self.get_form().instance
        CommunityMembership.objects.create(community=comm_obj, member=self.request.user, membership_type="admin")
        
        return reverse('community', args=[comm_obj.slug])
        

class CommunityListView(LoginRequiredMixin, generic.ListView):
    model = Community


class EntityListView(LoginRequiredMixin, generic.ListView):
    model = OtherEntity


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User


class CommunityDetailView(LoginRequiredMixin, generic.DetailView):
    model = Community


class EntityDetailView(LoginRequiredMixin, generic.DetailView):
    model = OtherEntity


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User


class ProfileView(LoginRequiredMixin, generic.FormView):
    def get_form_kwargs(self) -> dict[str, Any]:
        return {'instance': self.request.user}

    form_class = UserProfileForm
    template_name = "entities/user_form.html"
    success_url = "/"


class CommunityUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = CommunityForm
    template_name = "entities/community_form.html"

    def get_success_url(self) -> str:
        comm_obj = self.get_form().instance
        CommunityMembership.objects.create(community=comm_obj, member=self.request.user, membership_type="admin")
        
        return reverse('community', args=[comm_obj.slug])
        

