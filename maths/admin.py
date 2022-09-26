from django.contrib import admin
from .models import *

# Register your models here.


class SubmissionAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'user',
        'metric',
        'subject1',
        'subject2',
        'value',
        'file',
        'remarks',
    ]
    list_display_links = [
        'user',
        'metric',
    ]
    list_filter = [
        'date',
        'user',
        'metric',
        'value',
    ]
    search_fields = [
        'user__email',
        'metric'
    ]


admin.site.register(Submission, SubmissionAdmin)
