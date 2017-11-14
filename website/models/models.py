from django.db import models

# Create your models here.
from django.core.validators import RegexValidator

Numbers_validator = RegexValidator(r'^[0-9]*$', 'Only numbers are allowed.')
Zip_Code_validator = RegexValidator(r'^[0-9]*$', 'Input 5 digit Zip Code')
name_validator = RegexValidator(r"[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$", 'Enter a valid name.')
username_validator = RegexValidator(r'[a-z][a-z0-9_.-]*$',"Enter a valid username (Only lowercase, numbers, hyphens, underscores and dots are allowed.")
city_validator = RegexValidator(r"[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$", 'Enter a valid city.')
State_validator = RegexValidator(r"[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$", 'Enter a valid State.')
street_validator = RegexValidator(r"[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+[0-9]*$", 'Enter a valid street.')
pickup_arrangements_validator = RegexValidator(r"[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+[0-9]*$", 'Enter a valid pickup arrangements.')

'''
class User(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Email = models.EmailField(primary_key=True)
    Address_Line1 = models.CharField(max_length=100)
    Address_Line2 = models.CharField(max_length=100)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=2,validators=[State_validator])
    ZIP_Code = models.IntegerField(default=1, validators=[Zip_Code_validator])
    Country = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length = 20,validators=[Numbers_validator])
    Pickup_Arrangment = models.CharField(max_length=100)
    Preferred_Contact = models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name + self.Last_Name
'''