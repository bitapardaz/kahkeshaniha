from django.db import models

from django.contrib.auth.models import User
from content_management.models import Theme

class UserType(models.Model):

    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class UserProfile(models.Model):

    user = models.ForeignKey(User)
    mobile_number = models.CharField(max_length=20)

    otp = models.IntegerField(default=0)
    expiry_datetime = models.DateTimeField()

    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    user_type = models.ForeignKey(UserType)
    thumbnail = models.ImageField(upload_to="images")

    # some celebrities or profiles might have their shop activated.
    is_shop_activated = models.BooleanField(default=False)

    # vote allowance
    # for normal customers vote allowance is limited. for celebrities and admins
    # vote allowance is unlimited.
    # in the future, people may pay a subscription fee to be able to
    # vote unboundedly.
    is_vote_allowance_unlimited = models.BooleanField(default=False)
    vote_allowance = models.IntegerField(default=50)


    def __unicode__(self):
        return self.mobile_number

class UserInterest(models.Model):
    user = models.ForeignKey(User)
    theme = models.ForeignKey(Theme)
