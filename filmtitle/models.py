from django.db import models


class Film(models.Model):

    origname = models.CharField(max_length=255)
    uuid = models.CharField(max_length=50)
    rusname = models.CharField(max_length=255)

    def __str__(self):
        return self.origname

