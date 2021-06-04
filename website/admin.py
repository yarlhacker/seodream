from django.contrib import admin

from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title','date_create','date_update','status')
    list_editable =('status',)



@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image','date_create','date_update','status')
    list_editable =('status',)

    def image_views(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:20px; height:100px">')


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('date_create','date_update','status')
    list_editable =('status',)


@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('logo_site','nom_site','date_create','date_update','status')
    list_editable =('status',)

    def image_views(self, obj):
        return mark_safe(f'<img src="{obj.logo_site.url}" style="width:20px; height:100px">')


@admin.register(models.Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('nom_statistique','nom_statistique','date_create','date_update','status')
    list_editable =('status',)





# Register your models here.
