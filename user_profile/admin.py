from django.contrib import admin

from models import UserType,UserProfile,UserInterest
# Register your models here.
admin.site.register(UserType)
admin.site.register(UserProfile)
admin.site.register(UserInterest)
