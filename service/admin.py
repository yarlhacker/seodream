from django.contrib import admin

from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('number','nom','date_create','date_update','status')
    list_editable =('status',)


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','date_create','date_update','status')
    list_editable =('status',)


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('nom','image','date_create','date_update','status')
    list_editable =('status',)
    
    def image_views(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:20px; height:100px">')

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom','date_create','date_update','status')
    list_editable =('status',)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','surnom','nom','date_create','date_update','status')
    list_editable =('status',)
# Register your models here.
