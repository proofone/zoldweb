from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import User, Community, Location, OtherEntity


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {"username": UsernameField}  # TODO: add email field + others?
        

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Community
    # template_name = "entities/index.html"


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "entities/user_form.html"
    success_url = "/"


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
