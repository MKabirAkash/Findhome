from django.db import models
from datetime import datetime

class Contacts(models.Model):
    listing=models.CharField(max_length=200)
    listing_id=models.IntegerField()
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    message=models.CharField(max_length=200)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(blank=True)

    def __str__(self):
        return self.name
    

