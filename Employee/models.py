from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class PersonalDetail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

class Employee(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField()
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    mobileno = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    pic = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    
@receiver(sender=User,signal=post_save)
def after_save_user(sender,instance,created,**kwargs):
    if created:
        instance.is_staff=True
        instance.save()
        pd=PersonalDetail()
        pd.user=instance
        pd.save()
        t=Token()
        t.user=instance
        t.save()



