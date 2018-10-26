from django.contrib import admin
from .models import *


# Register your models here.

class DayNumberAdmin(admin.ModelAdmin):
    list_display = ['day', 'count']


class UseripAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'count']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'count']


admin.site.register(Userip, UseripAdmin)
admin.site.register(VisitNumber)
admin.site.register(DayNumber, DayNumberAdmin)
admin.site.register(PlayerNumber, PlayerAdmin)
