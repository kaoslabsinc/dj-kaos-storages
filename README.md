# DJ KAOS Storages

A set of django media storage classes for different use cases such as private file storage on S3. An extension
of [jschneier](https://github.com/jschneier) 's
[django-storages](https://github.com/jschneier/django-storages)

## Quick Start

```shell
pip install dj-kaos-storages
```

```python
# settings.py
import os

AWS_ACCESS_KEY_ID = os.environ['DJANGO_AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['DJANGO_AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['DJANGO_AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ.get('DJANGO_AWS_S3_REGION_NAME', None)

STORAGES_PUBLIC_MEDIA_LOCATION = 'media'
STORAGES_PRIVATE_MEDIA_LOCATION = 'private-media'
PUBLIC_FILE_STORAGE = 'kaos_storages.s3.PublicMediaFilesS3Storage'
PRIVATE_FILE_STORAGE = 'kaos_storages.s3.PrivateMediaFilesS3Storage'

# default being private
DEFAULT_FILE_STORAGE = PRIVATE_FILE_STORAGE
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{STORAGES_PRIVATE_MEDIA_LOCATION}/'
```

Now if somebody goes to the url `https://your-bucket.s3.amazonaws.com/private-media/path/to/your/file`, they would get a
403, effectively making your media files private. The project loads the private media assets by appending a signature
url param, that is only valid for a short period of time.

## Rationale

It is a good idea to not store user uploaded files (i.e. media files) on the server you are running your application in.
If you need to shut down the server, or it goes down for any reason, all those files are lost. Also storing user
uploaded files on a server would potentially take up a massive amount of storage space on the server. For that reason it
is better to store such files on a storage service such as S3. This package is an extension of
[django-storages](https://github.com/jschneier/django-storages) and allows a few more granular common use cases.

### Public vs Private media files

If you want media files to be only accessible through your application, and want to prevent users to put in the url in
their browsers and access the files, you'd want to use a private media file storage.

## AWS S3

dj-kaos-storage comes with 3 classes to handle external storage on Amazon S3. All the following classes require to add
necessary settings for `django-storages`. Refer to `django-storages`'s
[documentation](https://django-storages.readthedocs.io/en/latest/) for more details.

```python
AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env('DJANGO_AWS_S3_REGION_NAME', default=None)
```

### `StaticFilesS3Storage`

To store static files on S3. The management command `collectstaic` will put all your static files on S3 at the location
described by `settings.STORAGES_STATICFILES_LOCATION`. In order to use this class:

```python
# settings.py 
STORAGES_STATICFILES_LOCATION = 'static'  # or anything else for that matter
STATICFILES_STORAGE = 'kaos_storages.s3.StaticFilesS3Storage'
```

Note you can omit `settings.STORAGES_STATICFILES_LOCATION`, and by default it is set to `static`.

### `PublicMediaFilesS3Storage`

To store public media files on S3. In order to use:

```python
# settings.py 
STORAGES_PUBLIC_MEDIA_LOCATION = 'media'  # or anything else for that matter
PUBLIC_FILE_STORAGE = 'kaos_storages.s3.PublicMediaFilesS3Storage'
DEFAULT_FILE_STORAGE = PUBLIC_FILE_STORAGE
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{STORAGES_PUBLIC_MEDIA_LOCATION}/'
```

### `PrivateMediaFilesS3Storage`

To store private media files on S3. In order to use:

```python
# settings.py 
STORAGES_PRIVATE_MEDIA_LOCATION = 'private-media'  # or anything else for that matter
PRIVATE_FILE_STORAGE = 'kaos_storages.s3.PrivateMediaFilesS3Storage'
DEFAULT_FILE_STORAGE = PRIVATE_FILE_STORAGE
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{STORAGES_PRIVATE_MEDIA_LOCATION}/'
```

## Development and Testing

### IDE Setup

Add the `example` directory to the `PYTHONPATH` in your IDE to avoid seeing import warnings in the `tests` modules. If
you are using PyCharm, this is already set up.

### Running the Tests

Install requirements

```
pip install -r requirements.txt
```

For local environment

```
pytest
```

For all supported environments

```
tox
```
