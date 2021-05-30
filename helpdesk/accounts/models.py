from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()
# class User(auth.models.User,auth.models.PermissionsMixin):

#     def __str__(self):
#         return "@{}".format(self.username)

# Create your models here.
class UserDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{}".format(self.user.first_name)


