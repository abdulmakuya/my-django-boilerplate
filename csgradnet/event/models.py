from django.db import models

# Create your models here.
class event(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Description=models.TextField(max_length=500,null=True)
    eventDate=models.DateTimeField(max_length=50,null=True)
    eventVenue=models.CharField(max_length=50,null=True)
    eventFee=models.CharField(max_length=50,null=True)


    def  __str__(self):
        return self.Name
