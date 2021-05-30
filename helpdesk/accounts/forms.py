from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm
from accounts import models
from django import forms



class UserCreateForm(UserCreationForm):

    class Meta():
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model=models.UserDetails
        fields=['mobile','status','profile_pic']



class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserCreateForm,
        'details': UserDetailsForm,
    }
    def save(self, commit=True):
        objects = super(UserCreationMultiForm, self).save(commit=False)

        if commit:
            user = objects['user']
            user.save()
            details = objects['details']
            details.user = user
            details.save()

        return objects

    # success_urls = {
    #     'contact': reverse_lazy('contact-form-redirect'),
    #     'subscription': reverse_lazy('submission-form-redirect'),
    # }


