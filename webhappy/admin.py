from django.contrib import admin
from .models import MainPage, Slider, Partner, Wwd, Video

class Partner_Admin(admin.ModelAdmin):
    list_display = ('number','name','link')

admin.site.register(MainPage)
admin.site.register(Slider)
admin.site.register(Wwd)
admin.site.register(Video)
admin.site.register(Partner, Partner_Admin)