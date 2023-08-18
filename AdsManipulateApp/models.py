from django.db import models
import uuid 


# Create your models here.
class Sell(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    username = models.CharField(max_length=100)
    productName = models.TextField()
    image = models.ImageField(upload_to='product_images')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.username