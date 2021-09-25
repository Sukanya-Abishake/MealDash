from django.db import models
from accounts.models import Customer

# Create your models here.

class MenuItem(models.Model):

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250,blank=True)
    price = models.FloatField()
    #pieces = models.IntegerField(default=6)
    instructions = models.CharField(max_length=250,default="Available")
    image = models.ImageField(default='default.png', upload_to='images/')
    created_by =models.DateField(auto_now=True,null=True)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(
        'MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=15, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)

"""class CartItems(models.Model):
    ORDER_STATUS = (
        ('Active', 'Active'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    #ordered_date = models.DateField(auto_now=True,null=True)
    #status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Active')
    #delivery_date = models.DateField(auto_now=True,null=True)

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def _str_(self):
        return self.item.title
    
    def get_remove_from_cart_url(self):
        return reverse("main:remove-from-cart", kwargs={
            'pk' : self.pk
        })

    def update_status_url(self):
        return reverse("main:update_status", kwargs={
            'pk' : self.pk
        })"""