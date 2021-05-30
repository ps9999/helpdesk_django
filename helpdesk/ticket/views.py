from django.shortcuts import render
from .forms import TicketCreationForm
from django.shortcuts import render,redirect  
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,ListView
from . import models
from django.contrib.auth import get_user_model 
# user = get_user_model()

# Create your views here.

class TicketCreateView(CreateView):
    form_class = TicketCreationForm
    success_url = reverse_lazy('ticket:listTicket')
    template_name = 'ticket/create_ticket.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        tickets = form.save(commit=False)
        tickets.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ticket:listTicket')


class TicketListView(ListView):    
    template_name = 'ticket/ticket_list.html'
    model = models.Ticket