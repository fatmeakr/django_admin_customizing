from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from utils.validators import mobile_number_validator

UserModel = get_user_model()


class UpdateUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text="To change your password " 'use <a href="../password/">this form</a>.',
    )

    class Meta:
        model = UserModel
        fields = "__all__"


class CustomUserCreationForm(UserCreationForm):
    mobile_number = forms.CharField(
        label="Mobile", help_text="Mobile number must be entered in the format: '09999999999'.", validators=[mobile_number_validator], required=True
        )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].help_text = None
        del self.fields["password2"]
