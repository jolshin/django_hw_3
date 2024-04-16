from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)
    
    def __str__(self):
        return f'{self.name}, {self.price}, {self.release_date}, {self.lte_exists}, {self.slug}'
