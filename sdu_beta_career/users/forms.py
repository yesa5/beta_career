from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Profile

User = get_user_model()


class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User


class UserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'course',
            'gpa',
            'birth_date',
            'faculty',
            'linked_in',
            'github'
        )
        widgets = {
            'course': forms.NumberInput(attrs={'placeholder': 'Your course'}),
            'gpa': forms.NumberInput(attrs={'placeholder': 'Your GPA'}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'faculty': forms.Select(),
            'linked_in': forms.URLInput(attrs={
                'placeholder': 'Your linked-in account'
            }),
            'github': forms.URLInput(attrs={
                'placeholder': 'Your github account'
            }),
        }
