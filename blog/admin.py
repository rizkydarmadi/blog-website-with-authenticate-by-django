from django.contrib import admin

# Register your models here.
from .models import artikel

class artikeladmin(admin.ModelAdmin):
    readonly_fields=[
        'slug',
        'update',
        'published',
    ]

admin.site.register(artikel, artikeladmin)