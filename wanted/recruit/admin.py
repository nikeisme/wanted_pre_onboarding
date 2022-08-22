from django.contrib import admin
from .models import Notification,Company,User,Another


admin.site.register(Notification)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Another)