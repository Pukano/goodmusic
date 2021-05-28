from django.db import models

# Create your models here.

class ContactDetails(models.Model):
    #location =
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return str(self.id)
