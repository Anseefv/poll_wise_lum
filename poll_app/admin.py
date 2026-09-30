from django.contrib import admin
from poll_app.models import  CustomUser,Poll,Vote

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Poll)
admin.site.register(Vote)
