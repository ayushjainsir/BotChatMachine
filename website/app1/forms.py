from django.contrib.auth.models import user_logged_in
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registraionform(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1','password2']

        def save(self, commit=True):
            user = super(registraionform,self).save(commit=False)
            user.first_name = self.cleaned_data['username']
            user.first_name = self.cleaned_data['first_name']
            user.first_name = self.cleaned_data['last_name']
            user.first_name = self.cleaned_data['email']
            if commit:
                user.save()

            return user
