from django.contrib import admin

# Register your models here.
from appbook.models import User,ActivityPeriod

admin.site.register(User)
admin.site.register(ActivityPeriod)
