from django.contrib import admin
from . import models
from .models.tools import Tool
from .models.tools import Sharedtool, CommunityShed
# Register your models here.

from .models.users import User
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'Email',
    ]

    class Meta:
        model = User


class ToolAdmin(admin.ModelAdmin):
    pass


class SharedtoolAdmin(admin.ModelAdmin):
    pass


class CommunityShedAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.users.User, UserAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Sharedtool, SharedtoolAdmin)
admin.site.register(CommunityShed, CommunityShedAdmin)

