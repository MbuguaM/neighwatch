from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.
#models  
# user


# neighborhood
class Neighborhood(models.Model):
    """ class for mapping neighbourhood data """
    name  = models.CharField(max_length = 30, unique=True)
    location = models.CharField(max_length = 30)
    occupant_count = models.PositiveIntegerField(default = 0)
    hood_admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='neighborhood_images', blank=True)
    
    def __str__(self):
        return self.name

    # methods
    @classmethod
    def save_neigh(self,name, location):
        """ saving the neighborhood instance """
        neigh = cls(name =name, location=location)
        neigh.save()
        return neigh

    def delete_prof(self):
        """ deletes user instance """
        self.delete()

    @classmethod
    def find_neigborhood(cls,query):
        return cls.objects.filter(name__icontains = query)
#post model
class Posts(models.Model):
    """ model that handles comment data"""
    title = models.CharField(max_length  = 20, blank = True, null = True)
    comment = models.TextField()
    user_name  =models.CharField(max_length = 30)
    
    def __str__(self):
        return self.title

    # methods
    def save_post(self):
        """ saves user instance """
        self.save()

    def delete_post(self):
        """ deletes user instance """
        self.delete()

class Services(models.Model):
    """ class that saves the services data """
    neighborhood = models.ForeignKey(Neighborhood, on_delete= models.CASCADE)
    police_station = models.CharField(max_length = 30, null=True, blank =True)
    police_no = models.IntegerField( default=0)
    police_address = models.CharField(max_length = 30 ,blank = True, null = True)
    healthcare_centre = models.CharField(max_length = 30, blank =True, null =True)
    healthcare_no = models.IntegerField()
    healthcare_address = models.CharField(max_length  = 20, null = True , blank = True)

    def __str__(self):
        return self.police_station 

    # methods
    def save_prof(self):
        """ saves user instance """
        self.save()

    def delete_prof(self):
        """ deletes user instance """
        self.delete()



class User_prof(models.Model):
    """ class that saves the user data """
    # user_name = models.OneToONe(user,on_delete = 'models.CASCADE')
    image = models.ImageField(upload_to='user_images', blank=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE ,related_name ='profile')
    user_location = models.ForeignKey(Neighborhood, on_delete = models.CASCADE, null = True)
    mail_confirm = models.BooleanField(default = False)
    phone_num = models.IntegerField(null =True)
    def __str__(self):
        return self.user

    # methods
    def save_prof(self):
        """ saves user instance """
        self.save()

    def delete_prof(self):
        """ deletes user instance """
        self.delete()

    def delete(self):
        """ redifining the mail_confirm field in the user_prof"""
        self.mail_confirm = False
        self.save()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        User_prof.objects.create(user=instance)
    instance.profile.save()

 #bussinesses
class Bussiness(models.Model):
    """ model that displays the business in an area """
    bussiness_name = models.CharField(max_length = 30)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    Neighborhood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE)
    Email_adress = models.CharField(max_length = 30,null = True)
    image = models.ImageField(upload_to='business_images', blank=True)