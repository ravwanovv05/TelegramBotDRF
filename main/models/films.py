from django.db import models
from PIL import Image
from io import BytesIO
import os
from django.core.files import File
from main.models.categories import Category


class Film(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')
    language = models.CharField(max_length=255, null=True, blank=True, verbose_name='Language')
    size = models.CharField(max_length=255, null=True, blank=True, verbose_name='Size')
    release_date = models.CharField(max_length=10, null=True, blank=True, verbose_name='Release Date')
    file_unique_id = models.TextField(verbose_name='File Unique ID')
    message_id = models.BigIntegerField(null=True, blank=True, verbose_name='Message ID')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category ID')

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         image = Image.open(self.image)
    #         new_size = (300, 200)
    #
    #         resized_image = image.resize(new_size)
    #
    #         temp_io = BytesIO()
    #         resized_image.save(temp_io, format='JPEG')
    #         temp_io.seek(0)
    #
    #         image_name = os.path.basename(self.image.name)
    #         self.image.save(image_name, File(temp_io), save=False)
    #     super().save(*args, **kwargs)
    #
