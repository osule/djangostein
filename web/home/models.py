from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

image_storage = FileSystemStorage(
    # Physical file location ROOT
    location='{}/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url='{}/'.format(settings.MEDIA_URL),
)

def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/dashboard/picture/<filename>
    return 'photos/profils/{}'.format(filename)

def logo_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/dashboard/picture/<filename>
    return 'photos/logos/{}'.format(filename)


# Create your models here.
class Photo(models.Model):
    img = models.ImageField(
        upload_to=image_directory_path,
        storage=image_storage,
        blank=True,
        verbose_name='Image')

    @property
    def url(self):
        return '{}{}'.format(settings.MEDIA_URL, self.img)