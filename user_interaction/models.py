from django.contrib.auth.models import User

from django.db import models
from content_management.models import Content

#a user may follow another user
class UserAssociation(models.Model):
    source = models.ForeignKey(User,related_name='source')
    destination = models.ForeignKey(User,related_name='desination')
    date_time = models.DateTimeField()


# a user might like another user's content
class LikeContent(models.Model):
    user = models.ForeignKey(User)
    content = models.ForeignKey(Content)
    date_time = models.DateTimeField(auto_now=True)


# a user might vote up another user's content
class VoteType(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


# a user might vote up another user's content
# a vote might be from a celebrity
class VoteContent(models.Model):
    user = models.ForeignKey(User)
    date_time = models.DateTimeField(auto_now=True)
    vote_type = models.ForeignKey(VoteType)


# a user might leave comment for another user.
# we assume all comments are abusive unless proven otherwise.
# a comment might be from a celebrity
class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.ForeignKey(Content)
    date_time = models.DateTimeField(auto_now=True)
    is_abusive = models.BooleanField(default=True)
    text = models.CharField(max_length=100)

# a celebrity might choose a content as his/her approved contnet.
class ChosenForTalent(models.Model):
    user = models.ForeignKey(User)
    content = models.ForeignKey(Content)
    date_time = models.DateTimeField(auto_now=True)
