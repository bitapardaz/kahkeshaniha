from django.contrib import admin

# Register your models here.
from models import UserAssociation,LikeContent,VoteType,VoteContent,Comment,ChosenForTalent

admin.site.register(UserAssociation)
admin.site.register(LikeContent)
admin.site.register(VoteType)
admin.site.register(VoteContent)
admin.site.register(Comment)
admin.site.register(ChosenForTalent)
