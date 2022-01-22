from django.contrib import admin

from .models import DefaultFileUpload, PublicFileUpload, PrivateFileUpload

admin.site.register(DefaultFileUpload)
admin.site.register(PublicFileUpload)
admin.site.register(PrivateFileUpload)
