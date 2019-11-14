from django.contrib import admin
from albumapp import models

# class albumadmin(admin.ModelAdmin):
#     list_display = ('Alocation','Atitle','Adesc')

admin.site.register(models.AlbumModel)
admin.site.register(models.PhotoModel)
