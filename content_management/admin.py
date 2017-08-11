from django.contrib import admin

# Register your models here.
from models import ContentType,Theme,Content

admin.site.register(ContentType)
admin.site.register(Theme)
admin.site.register(Content)
