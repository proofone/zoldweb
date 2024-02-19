import logging
from typing import Any
from urllib.parse import urlencode
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .forms import CommunityForm, RegisterForm, UserProfileForm, EntityForm
from .models import User, Community, CommunityMembership, Location, OtherEntity, Invitation


logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "brahma/index.html"


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "entities/user_form.html"
    success_url = "/"

    # TODO: def get() -> check invitation id w. regex + inv. obj
    
    def get_initial(self) -> dict[str, Any]:
        initials = super().get_initial()
        initials['email'] = self.request.GET.get('ie', "")

        return initials

    def form_valid(self, form):
        if self.request.POST.get('inv_id', None):
            try:
                inv_obj = Invitation.objects.get(pk=self.request.POST['inv_id'])
                if inv_obj.invitee:
                    logger.warning(f"Invitation with ID already used: {form.cleaned_data['inv_id']}")
                    form.instance.is_active = False
                    # TODO: inform user & ask confirmation / reject
                    
                else:
                    self.object = form.save()
                    inv_obj.invitee = self.object
                    inv_obj.save()

            except Invitation.DoesNotExist:
                logger.warning(f"Nonexistent invitation ID: {form.cleaned_data['inv_id']}")
                form.instance.is_active = False
                # TODO: inform user

        if not self.object:
            self.object = form.save()

        return HttpResponseRedirect(reverse('home'))
        

class ConfirmEmailView(generic.TemplateView):
    pass  #TODO
        

class SendInvitationView(LoginRequiredMixin, generic.CreateView):
    model = Invitation
    fields = ["email"]
    success_url = "/" # reverse('profile')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        self.object = form.save()
        email_context = {
            'sender': str(self.request.user),
            'site_name': settings.SITE_TITLE,
            'site_url': self.request.get_host(),
            'invitation_url': self.request.get_host() + reverse('register') + "?" + urlencode((("iid", self.object.pk),("ie", self.object.email),)),
            }
        
        send_mail("Meghívó - " + settings.SITE_TITLE,
                  render_to_string("email/invitation.txt", email_context, self.request),
                  None,
                  [self.object.email],
                  html_message=render_to_string("email/invitation.html", email_context, self.request)) #TODO
        
        return HttpResponseRedirect(reverse("send-invitation"))


class CommunityCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CommunityForm
    template_name = "entities/community_form.html"

    def get_success_url(self) -> str:
        comm_obj = self.get_form().instance
        CommunityMembership.objects.create(community=comm_obj, member=self.request.user, membership_type="admin")
        
        return reverse('community', args=[comm_obj.slug])


class EntityCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = EntityForm
    template_name = "entities/community_form.html"

    def get_success_url(self) -> str:
        ent_obj = self.get_form().instance
        
        return reverse('otherentity', args=[ent_obj.slug])
        

class CommunityListView(LoginRequiredMixin, generic.ListView):
    model = Community
    extra_context = {'title': Community._meta.verbose_name}
    # TODO: refactor: standard views with iteration, page titles as ctxt variable


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
        

