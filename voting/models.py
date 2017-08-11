from django.db import models

from content_management.models import Content
from django.contrib.auth.models import User

# captures the content that are seen in by a user when voting.
# the use must not see duplicate content when going through the candidates.
class ContentViewLog(models.Model):
    content = models.ForeignKey(Content)
