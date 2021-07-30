from django.db import models

from kaos_storages.fields import PublicFileField, PrivateFileField


class DefaultFileUpload(models.Model):
    file = models.FileField(upload_to='default')


class PublicFileUpload(models.Model):
    file = PublicFileField(upload_to='public')


class PrivateFileUpload(models.Model):
    file = PrivateFileField(upload_to='private')
