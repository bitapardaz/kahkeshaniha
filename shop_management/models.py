from django.db import models

from content_management.models import Content
from django.contrib.auth.models import User

class AllowanceItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    order = models.IntegerField(default=0)


# Create your models here.
class AllowancePurchase(models.Model):
    date_time = models.DateTimeField()
    token = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    item = models.ForeignKey(AllowanceItem)


class PurchasedContent(models.Model):
    user = models.ForeignKey(User)
    content = models.ForeignKey(Content)
    date_time = models.DateTimeField(auto_now=True)
    rrn = models.CharField(max_length=100)
