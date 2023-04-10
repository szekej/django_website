from django import forms
from first_app.models import UserAll, UserProfileInfo
from django.contrib.auth.models import User
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label_suffix='')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail:
            raise forms.ValidationError("Emails should be the same")


class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserAll
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')