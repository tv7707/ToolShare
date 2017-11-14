from django.db import models
from website.models.users import User

class CommunityShed(models.Model):
    ShedName = models.CharField(max_length=20)
    ShedStreetAddress = models.CharField(max_length=20)
    ShedStreetAddress2 = models.CharField(max_length=20)
    ShedCity =  models.CharField(max_length=20)
    ShedState =  models.CharField(max_length=20)
    ShedZip =  models.CharField(max_length=20)
    is_Active = models.BooleanField(default=False)
    ShedCoord = models.ForeignKey(User)


    def __str__(self):
        return self.ShedName
