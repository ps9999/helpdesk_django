from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm
from betterforms.multiform import MultiModelForm
from accounts import models
from django import forms
from .models import Ticket

class TicketCreationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('ticket_code','category','issue','priority',
        'area','email','description','corrective_action','preventive_action','rca_desc',
        'image_description','image','email_on_update','email_on_closure','ticket_status')
        

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['city'].queryset = City.objects.none()


