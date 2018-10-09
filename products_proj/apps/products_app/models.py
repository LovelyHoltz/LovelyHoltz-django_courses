from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 1000)
    product_weight = models.IntegerField(default= 1000)
    product_category = models.CharField(max_length = 50)
    product_cost = models.IntegerField(default = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
