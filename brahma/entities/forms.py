from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms.renderers import TemplatesSetting
from django.forms import ModelForm
from .models import Community, OtherEntity


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


class EntityForm(BootstrapForm, ModelForm):
    class Meta:
        model = OtherEntity
        fields = ['name', 'category', 'intro',
                  'hometown', 'phone', 'avatar_photo']


class CommunityForm(BootstrapForm, ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'status', 'intro',
                  'hometown', 'phone', 'avatar_photo',
                  'founded', 'slug']


class UserProfileForm(BootstrapForm, ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", 'avatar_photo', 'intro',
                  'hometown', 'phone']


class RegisterForm(UserCreationForm, BootstrapForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", )
        field_classes = {"username": UsernameField}
