from django.db import models

from ToolsShareProject import settings


class USStates:
    states_list = (
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AS", "American Samoa"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("DC", "District Of Columbia"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("GU", "Guam"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("MP", "Northern Mariana Islands"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("PR", "Puerto Rico"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UM", "United States Minor Outlying Islands"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VI", "Virgin Islands"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WV", "West Virginia"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming")
    )

    def get_long_name(self, abbreviation):
        return dict(self.states_list).get(abbreviation)

class Pref_Contact(models.Model):
    Contact_CHOICES = (
        ('P', 'Phone'),
        ('E', 'Email'),
    )

class Pickup_arrengment(models.Model):
    Contact_CHOICES = (
        ('S', 'Self'),
        ('H', 'Home Delivery'),

    )

# from django.contrib.auth.models import User
# from django.contrib.auth.validators import ASCIIUsernameValidator

# Create your models here.
from django.core.validators import RegexValidator

Phone_validator  = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+0123456789'. Up to 15 digits allowed.")
Numbers_validator = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed!')
Zip_Code_validator = RegexValidator(regex=r'^[0-9][0-9][0-9][0-9][0-9]$',message= "Enter 5 digit Zip Code!")
Names_validator = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabetic characters are allowed!')

class User(models.Model):
    First_Name = models.CharField(max_length=20,validators=[Names_validator])
    Last_Name = models.CharField(max_length=20,validators=[Names_validator])
    #Age = models.DateField(null=True, blank=True)
    Date_of_Birth = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Email = models.EmailField(primary_key=True)
    Address_Line1 = models.CharField(max_length=100)
    Address_Line2 = models.CharField(max_length=100)
    City = models.CharField(max_length=20, validators=[Names_validator])
    State = models.CharField(max_length=50,  choices=USStates.states_list)
    ZIP_Code = models.IntegerField(max_length=5,validators=[Zip_Code_validator])
    Country = models.CharField(max_length=100, validators=[Names_validator])
    Phone_Number = models.CharField(max_length = 20,validators=[Phone_validator])
    Pickup_Arrangment = models.CharField(max_length=100,choices=Pickup_arrengment.Contact_CHOICES)
    Preferred_Contact = models.CharField(max_length=100,choices=Pref_Contact.Contact_CHOICES)
    seen=models.IntegerField(max_length=5, default=0)

    def __str__(self):
        return self.First_Name + " " + self.Last_Name
