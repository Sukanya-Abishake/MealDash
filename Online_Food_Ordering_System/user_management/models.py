from django.db import models

# Create your models here.
class Customer(models.Model):
    """Model representing a Customer."""
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    pincode = models.IntegerField(blank=True)
    profile_img = models.ImageField(upload_to='Profile_images',default='default.png')


    def get_absolute_url(self):
        """Returns the url to access a detail record for this customer."""
        return reverse('customer-detail', args=[str(self.id)])   
        
    def __str__(self):
        """String for representing the Model object."""
        return self.name  


