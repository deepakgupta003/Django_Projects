from datetime import date
from pyexpat import model
from django.db import models

#Created a model by deepak to store details from contact page
#makemigrations = create changes in model and stor in a file
#migrate = apply the pending changes created by makemigrations

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateTimeField()

    #def __str__(self):
    #    return self.name,self.phone,self.phone,self.email