from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ('question','pub_date','was_published_recently')
    fieldsets = [
        ('Question', {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date']}),

    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date','question']
    search_fields = ['question']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)