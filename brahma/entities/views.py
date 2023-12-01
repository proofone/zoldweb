from django.conf import settings
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms.renderers import DjangoDivFormRenderer, TemplatesSetting
from django.template.loader import get_template

from django.contrib.auth import get_user_model
from .models import User, Community, Location, OtherEntity


class BootstrapFormRenderer(TemplatesSetting):
    form_template_name = "forms/form_bs5.html"


class BootstrapForm(ModelForm):
    default_renderer = BootstrapFormRenderer

    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.localize = True

            if field.field.widget.attrs.get('class', ""):
                field.field.widget.attrs['class'] += ' form-control mt-2'
            else:                
                field.field.widget.attrs['class'] = 'form-control mt-2'


class RegisterForm(UserCreationForm, BootstrapForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", )
        field_classes = {"username": UsernameField}


class CommunityCreateForm(BootstrapForm, ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'intro', 'location', 'founded']


class IndexView(generic.TemplateView):
    template_name = "brahma/index.html"


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "entities/user_form.html"
    success_url = "/"


class CommunityCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CommunityCreateForm
    template_name = "entities/community_form.html"
    success_url = "/"
        

class CommunityListView(LoginRequiredMixin, generic.ListView):
    model = Community


class EntityListView(LoginRequiredMixin, generic.ListView):
    model = OtherEntity


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User


class CommunityDetailView(LoginRequiredMixin, generic.DetailView):
    model = Community


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User


class EntityDetailView(LoginRequiredMixin, generic.DetailView):
    model = OtherEntity


