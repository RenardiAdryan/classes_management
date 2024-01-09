from django.contrib import admin
from core.models import *

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)

class ClassesAdmin(admin.ModelAdmin):
    list_display = ['name','updated_at','created_at']
    search_fields = ['name',]
admin.site.register(Classes,ClassesAdmin)
