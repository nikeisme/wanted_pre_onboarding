from django.contrib import admin
from .models import Notification
from .models import Company
from .models import User

admin.site.register(Notification)
admin.site.register(Company)
admin.site.register(User)
