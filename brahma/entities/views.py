from django.conf import settings
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

    def get_template(self, template_name):
        return get_template(template_name)


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", )
        field_classes = {"username": UsernameField}

    # template_name = "brahma/form_bs5.html"
    default_renderer = BootstrapFormRenderer

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if field.field.widget.attrs.get('class', ""):
                field.field.widget.attrs['class'] += ' form-control mt-2'
            else:                
                field.field.widget.attrs['class'] = 'form-control mt-2'


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Community
        

class CommunityListView(LoginRequiredMixin, generic.ListView):
    model = Community


class EntityListView(LoginRequiredMixin, generic.ListView):
    model = OtherEntity


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "entities/user_form.html"
    success_url = "/"
        

class CommunityCreateView(LoginRequiredMixin, generic.CreateView):
    model = Community
    fields = ['name', 'intro', 'location', 'founded']


class CommunityDetailView(LoginRequiredMixin, generic.DetailView):
    model = Community


def userlist(request, ):
    
    return None


def userdetail(request, ):
    
    return render(request, '../')

def communitylist(request, ):
    return None

def communitydetail(request, ):
    return None

def communitymap(request, ):
    return None

def otherentitylist(request, ):
    return None

def otherentitydetail(request, ):
    return None

def otherentitymap(request, ):
    return None
