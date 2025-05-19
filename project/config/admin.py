from django.contrib import admin

from .models import DefaultConfig, Participant


admin.site.register(DefaultConfig)
admin.site.register(Participant)