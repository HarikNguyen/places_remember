from django.db import models
from django.conf import settings
from django.contrib.gis.db import models as gis_model

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True, null=True)
    comment = models.TextField(blank=True)
    location = gis_model.PointField(srid=4326, geography=True, null=True, blank=True)

    def __str__(self):
        return self.name