from ticket.models import Department, Ticket, TicketCategory, TicketPriority, TicketStatus
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(Department)
admin.site.register(TicketStatus)
admin.site.register(TicketCategory)
admin.site.register(TicketPriority)
admin.site.register(Ticket)
