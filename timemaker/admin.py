from django.contrib import admin
from timemaker.models import Content

# Register your models here.
#admin.site.register(Content)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'site', 'url', 'start', 'end')
    list_display_links = ('id', 'site',)

admin.site.register(Content, ContentAdmin)
