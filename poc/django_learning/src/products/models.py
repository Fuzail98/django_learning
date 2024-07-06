from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000) # decimal_places and max_digits = required
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False) # null=True, default=True/False





# blank: It has to do with how the field is rendered (it is like required)
# null: It has do with database 