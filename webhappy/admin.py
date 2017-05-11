from django.contrib import admin
from .models import MainPage, Slider, Partner

class Partner_Admin(admin.ModelAdmin):
    list_display = ('number','name','link')

admin.site.register(MainPage)
admin.site.register(Slider)
admin.site.register(Partner, Partner_Admin)