from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect  
from django.urls import reverse_lazy,reverse
from . import forms
from django.views.generic import CreateView
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreationMultiForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        # Save the user first, because the profile needs a user before it
        # can be saved.
        user = form['user'].save()
        details = form['details'].save(commit=False)
        details.user = user
        details.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:login')




   



