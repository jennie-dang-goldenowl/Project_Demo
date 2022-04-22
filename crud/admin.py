from django.contrib import admin
from crud.models import *

class DeveloperModelAdmin(admin.ModelAdmin):
    # list_filter = ('dev')
    list_display = ('first_name', 'last_name','projects', 'language')
    search_fields = ['first_name', 'last_name']
    list_filter = ['language']

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'cost', 'developers',)
    search_fields = ['name']

# Register your models here.
admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Developer, DeveloperModelAdmin)