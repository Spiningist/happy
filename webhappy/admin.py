from django.contrib import admin
from .models import MainPage, Slider, Partner, Wwd, Video, How_to_help, Media, Media_images

class Partner_Admin(admin.ModelAdmin):
    list_display = ('number','name','link')

class Media_image_inline(admin.TabularInline):
    model = Media_images
    extra = 3

class Media_admin(admin.ModelAdmin):
    inlines = [ Media_image_inline, ]

admin.site.register(MainPage)
admin.site.register(Slider)
admin.site.register(Wwd)
admin.site.register(Video)
admin.site.register(Partner, Partner_Admin)
admin.site.register(How_to_help)
admin.site.register(Media, Media_admin)
