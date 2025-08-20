from django.forms import ModelForm, modelformset_factory
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import generic
from django.forms.renderers import TemplatesSetting
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EventSession


class BootstrapEventFormRenderer(TemplatesSetting):
    form_template_name = "forms/form_bs5_events.html"


class EventsForm(ModelForm):
    default_renderer = BootstrapEventFormRenderer

    class Meta:
        model = EventSession
        fields = ["start_date", "name", "holder", "cam_operator", "rec_needed"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the fields to read-only
        for field_name in ["start_date", "name", "holder"]:
            self.fields[field_name].widget.attrs["readonly"] = True 
               

   
EventsFormSet = modelformset_factory(
    EventSession,
    form=EventsForm
    )
    

class EventsBulkEditView(LoginRequiredMixin, generic.FormView):
    template_name = "events/events_bulk_edit.html"  # Specify your template
    success_url = "/events/"  # Redirect URL after successful form submission
    form_class = EventsForm
    
    queryset = None

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        qs = EventSession.objects.filter(start_date__isnull=False)
        formset = EventsFormSet(queryset=qs)
        return self.render_to_response(self.get_context_data(formset=formset))

    def post(self, request, *args, **kwargs):
        qs = EventSession.objects.filter(start_date__isnull=False)
        formset = EventsFormSet(request.POST, queryset=qs)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(self.success_url)
        return self.render_to_response(self.get_context_data(formset=formset))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formset"] = kwargs.get("formset")
        return context
