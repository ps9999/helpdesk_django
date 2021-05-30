from django.urls import path, re_path
from . import views

app_name = 'ticket'

urlpatterns = [
    re_path(r'^create/$', views.TicketCreateView.as_view(), name='createTicket'),
    re_path(r'^list/$', views.TicketListView.as_view(), name='listTicket'),
]