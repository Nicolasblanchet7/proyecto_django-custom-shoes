
from django.db import models

class ShoeModel(models.Model):
    name = models.CharField(max_length=100)
    base_image = models.ImageField(upload_to='shoes/base_images/')

    def __str__(self):
        return self.name

class ShoeCustomization(models.Model):
    shoe = models.ForeignKey(ShoeModel, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True, null=True)
    lace_color = models.CharField(max_length=50, blank=True, null=True)
    sole_size = models.CharField(max_length=20, blank=True, null=True)
    shape = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Customization for {self.shoe.name}'
