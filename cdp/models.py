from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(blank=True, null=False, )
    def __str__(self):
        return self.title

class CDP(models.Model):
    cmf = models.CharField(max_length=8)
    client_name = models.CharField(max_length=120)
    device_name = models.CharField(max_length=120, null=True)
    device_ip = models.CharField(max_length=15)
    cdp_scrape = models.TextField(blank=True, null=True)
    interface_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.client_name

