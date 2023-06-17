from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blogs)

class InternshipAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email',
                    'company',
                    'offer',
                    'start',
                    'end',
                    'timestamp')
    search_fields=('name', 'email', 'company')
    list_filter=['offer', 'start', 'end', 'timestamp']


admin.site.register(Internship, InternshipAdmin)           
