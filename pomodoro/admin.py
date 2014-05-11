from django.contrib import admin
from pomodoro.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'due_date', 'estimated_pomos', 'pomos_completed', 'seconds_completed', 'status', 'priority')
    list_filter = ['status']
    search_fields = ['name']

admin.site.register(Activity, ActivityAdmin)

