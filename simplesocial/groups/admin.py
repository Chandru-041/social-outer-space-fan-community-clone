from django.contrib import admin
from . import models

# GROUPS ADMIN.PY
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
