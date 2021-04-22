from django.contrib import admin
from ShortenerApp.models import UrlData

# Register your models here.


class UrlDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(UrlData, UrlDataAdmin)
