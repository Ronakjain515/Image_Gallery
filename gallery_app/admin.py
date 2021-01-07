from django.contrib import admin
from .models import ImagePost, Tags, Images
# Register your models here.


# class TagsInline(admin.TabularInline):
#     model = Tags
#
#
# class ImagesInline(admin.TabularInline):
#     model = Images
#
#
# class ImagePostAdmin(admin.TabularInline):
#     inlines = [
#         TagsInline,
#         ImagesInline
#     ]
admin.site.register(ImagePost)
admin.site.register(Tags)
admin.site.register(Images)
