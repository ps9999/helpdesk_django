from django.core.exceptions import AppRegistryNotReady
from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()

class Department(models.Model):
    department = models.CharField(max_length=70)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.department

class TicketCategory(models.Model):
    category=models.CharField(max_length=64)
    status = models.BooleanField(default=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.category

class TicketPriority(models.Model):
    priority=models.CharField(max_length=10)
    status=models.BooleanField(default=True)
    escalation_time=models.PositiveIntegerField()

    def __str__(self):
        return self.priority


class TicketStatus(models.Model):
    ticket_status=models.CharField(max_length=10)


    def __str__(self):
        return self.ticket_status





class Ticket(models.Model):
    ticket_code=models.CharField(max_length=50)
    category=models.ForeignKey(TicketCategory,on_delete=models.CASCADE)
    issue=models.CharField(max_length=1000)
    priority=models.ForeignKey(TicketPriority,on_delete=models.CASCADE)
    level=models.CharField(max_length=50,default='1')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    area=models.CharField(max_length=50,null=True,blank=True)
    ticket_status=models.ForeignKey(TicketStatus,on_delete=models.CASCADE)
    email=models.CharField(max_length=50,null=True,blank=True)
    email_on_update=models.BooleanField(default=True)
    email_on_closure=models.BooleanField(default=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    on_hold_till=models.PositiveIntegerField(null=True,blank=True)
    corrective_action=models.CharField(max_length=500,null=True,blank=True)
    preventive_action=models.CharField(max_length=500,null=True,blank=True)
    rca_desc=models.CharField(max_length=500,null=True,blank=True)
    status=models.BooleanField(default=True)
    image_description = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='ticket/',null=True,blank=True)

    def __str__(self):
        return self.ticket_code
    




