from django.forms import ModelForm, modelformset_factory
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EventSession


EventsFormSet = modelformset_factory(
    EventSession,
    fields = ["name", "holder", "cam_operator"]
    ),
    


class EventsBulkEditView(generic.FormView):
    formset = EventsFormSet()
