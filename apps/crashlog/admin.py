from django.contrib import admin

from crashlog.models import ErrorBatch, Error

class ErrorBatchAdmin(admin.ModelAdmin):
    list_display    = ('class_name', 'message', 'last_seen', 'times_seen', 'url', 'server_name')
    list_filter     = ('class_name', 'times_seen', 'server_name')
    ordering        = ('-last_seen',)

class ErrorAdmin(admin.ModelAdmin):
    list_display    = ('class_name', 'message', 'datetime', 'url', 'server_name')
    list_filter     = ('class_name', 'datetime', 'server_name')
    ordering        = ('-datetime',)

admin.site.register(ErrorBatch, ErrorBatchAdmin)
admin.site.register(Error, ErrorAdmin)

