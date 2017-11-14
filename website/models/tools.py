from django.db import models
from django.forms import ImageField
import os
from ToolsShareProject import settings
from website.models.users import User
from django.utils import timezone
from django.core.validators import RegexValidator
Names_validator = RegexValidator(r'^[a-zA-Z 0-9 ]*$', 'Name should consist of only alphabet and numbers!')

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

# Create your models here.
class Tool(models.Model):
    SHARE_LOCATION_CHOICES = (
        ('S', 'Shed'),
        ('H', 'Home'),
    )

    Tool_Name = models.CharField(max_length=20, validators=[Names_validator])
    share_date = models.DateField()
    avail_from = models.DateField()
    avail_to = models.DateField()
    message = models.CharField(max_length=500, default='None')
    Owner = models.ForeignKey(User, related_name='owner', default='None')
    Description = models.CharField(max_length=200,validators=[Names_validator])
    Condition = models.CharField(max_length=20,validators=[Names_validator])
    Is_active = models.BooleanField(default=True)
    Share_location= models.CharField(max_length=1, choices=SHARE_LOCATION_CHOICES)
    # It is NULL if tool is not shared as "Other" location
    #Share_location = models.CharField(max_length=200, blank=True, null=True)
    MinAge = models.IntegerField(default=10)
    picture = models.FileField()
    shed = models.ForeignKey(CommunityShed)

    def __str__(self):
        return self.Tool_Name

class Sharedtool(models.Model):

    STATUS_CHOICES = (
        ('Shared', 'Shared'),
        ('BorrowRequest', 'BorrowRequest'),
        ('Borrowed', 'Borrowed'),
        ('ReturnRequest', 'ReturnRequest'),
        ('Returned', 'Returned'),
        ('Declined', 'Declined'),
    )

    atool = models.ForeignKey(Tool, related_name='sharing')
    Borrower = models.ForeignKey(User, related_name='borrower', default='None')
    start_date = models.DateField('Start Date', default=timezone.now)
    end_date = models.DateField('End Date', default=timezone.now)
    #status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='BorrowRequest')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='BorrowRequest')
    message = models.CharField(max_length=500, default='None')
    owner_message = models.CharField(max_length=500, default='None')

    def __str__(self):
        thetool=self.atool
        return thetool.Tool_Name

