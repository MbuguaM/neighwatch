from django.db import models

# Create your models here.
#models  
# user
class user_profile(models.Model):
    """ class that saves the user data """
    # user_name = models.OneToONe(user,on_delete = 'models.CASCADE')
    user = models.OneToOneField(User, on_delete = 'models.CASCADE')
    user_location = models.ForeignKey(Neighborhood, on_delete = 'models.CASCADE')
    mail_confirm = models.BooleanField(default = True)

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
    

# neighborhood
class Neighborhood(models.Model):
    """ class for mapping neighbourhood data """
    name  = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    bussiness = models.OneToMany(Bussiness, on_delete = models.CASCADE)
    occupant_count = models.IntegerField()
    services = models.ForeignKey(Services, on_delete= 'models.CASCADE')
    
     def __str__(self):
        return self.user

    # methods
    def save_prof(self):
        """ saves user instance """
        self.save()

    def delete_prof(self):
        """ deletes user instance """
        self.delete()

#bussinesses
class Bussiness(models.Model):
    """ model that displays the business in an area """
    bussiness_name = models.CharField(max_length = 30)
    user = models.ForeignKey(user_profile, on_delete = 'models.CASCADE')
    Neighborhood = models.ForeignKey(Neighborhood, on_delete = 'models.CASCADE')
    Email_adress = models.CharField(max_length = 30)


#post model
class Posts(models.Model):
    """ model that handles comment data"""
    title = models.CharField(max_length  = 20)
    comment = models.TextField()
    user_name  =models.CharField(max_length = 30)
    
     def __str__(self):
        return self.user

    # methods
    def save_prof(self):
        """ saves user instance """
        self.save()

    def delete_prof(self):
        """ deletes user instance """
        self.delete()

class Services(models.Model):
    """ class that saves the services data """
    police_station = models.CharField(max_length = 30)
    police_no = models.IntegerField(10)
    police_address = models.CharField(max_length = 30)
    healthcare_centre = model.CharField(max_length = 30)
    healthcare_no = models.IntegerField(10)
    healthcare_address = models.CharField

     def __str__(self):
        return self.user

    # methods
    def save_prof(self):
        """ saves user instance """
        self.save()

    def delete_prof(self):
        """ deletes user instance """
        self.delete()