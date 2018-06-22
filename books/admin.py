# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Books



class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
    '__str__', 'action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message')
    list_filter = ('content_type',)
    search_fields = ['user__username', ]
    date_hierarchy = 'action_time'


admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(Books)

# Register your models here.
