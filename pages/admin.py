from django.contrib import admin
from .models import Property
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title','location','area','price','proptery_type')
    list_display_links = ('title',)
    list_filter =('proptery_type',)
    search_fields = ('title',)
    # fields =('title',)
admin.site.register(Property,PropertyAdmin)