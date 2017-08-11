from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class ContentType(models.Model):
    title = models.CharField(max_length=100)


class Theme(models.Model):
    title = models.CharField(max_length=50)
    order = models.IntegerField(default=0)


class Content(models.Model):
    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now=True)

    # is this content advertised in the user's talent page?
    is_included_in_my_talent = models.BooleanField(default=False)

    # order
    order = models.IntegerField(default=0)

    # number of likes
    number_of_likes = models.IntegerField(default=0)

    # upvote and downvote
    number_of_upvotes = models.IntegerField(default=0)
    number_of_downvotes = models.IntegerField(default=0)

    # number of views
    view_count = models.IntegerField(default=0)

    theme = models.ForeignKey(Theme)

    # if for the owner of this content shop_activated=True, then the owner
    # can put a price on its item.
    price = models.IntegerField(default=0)
