from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TechType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

class Meta:
    db_table='techtype'

class Product(models.Model):
    productname=models.CharField(max_length=255)
    producttype=models.ForeignKey(TechType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    producturl=models.URLField()
    description=models.TextField()

    def discountAmount(self):
        self.discount=self.price * .05
        return self.discount

#need to figure out why this is not working
#something to do with the function itself
    def discountPrice(self):
        disc=self.discountAmount()
        self.discountedPrice=self.price-self.disc 

    def __str__(self):
        return self.productname

class Meta:
    db_table='product'

class Review(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.title

class Meta:
    db_table='review'