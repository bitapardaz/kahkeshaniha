from django.db import models
from django.contrib.auth.models import User

class ContentType(models.Model):
    title = models.CharField(max_length=100)

class TalentBanner(models.Model):
    content_link = models.CharField(max_length=1000)
    content_type = models.ForeignKey(ContentType)
    order = models.IntegerField(default=100)

class JudgePageBanner(models.Model):
    judge = models.ForeignKey(User)
    content_link = models.CharField(max_length=1000)
    content_type = models.ForeignKey(ContentType)
    order = models.IntegerField(default=100)
