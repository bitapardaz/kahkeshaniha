from django.db import models

from content_management.models import Theme
# Create your models here.
class Contest(models.Model):
    theme = models.ForeignKey(Theme)
    is_currently_active = models.BooleanField(default=False)
