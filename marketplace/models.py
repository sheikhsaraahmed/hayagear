from django.db import models

class Designer(models.Model):
    brand_name = models.CharField(max_length=100)
    instagram_link = models.URLField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price_range = models.CharField(max_length=50)

    def __str__(self):
        return self.name
