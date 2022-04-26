from django.db import models
from django.contrib.gis.db import models as gis_models


class Provider(models.Model):
    def __str__(self):
        return self.name if self.name else self.email

    name = models.CharField('name', null=True, blank=True, max_length=100)
    email = models.EmailField('email', unique=True, max_length=100)
    phone_number = models.CharField(
        'phone number', null=True, blank=True, max_length=20)
    language = models.CharField(
        'language', null=True, blank=True, max_length=20)
    currency = models.CharField(
        'currency', null=True, blank=True, max_length=5)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    class Meta:
        verbose_name = "Provider"


class Area(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', max_digits=12, decimal_places=2)
    region = gis_models.PolygonField('region', blank=True, null=True)
    provider = models.ForeignKey(
        Provider,
        related_name='areas',
        on_delete=models.CASCADE,
        verbose_name='areas')
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)

    class Meta:
        verbose_name = "Service Area"
