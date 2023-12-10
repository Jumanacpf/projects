from django.db import models

# Create your models here.
class account(models.Model):
    accno=models.IntegerField()
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    amount=models.IntegerField()



    def __str__(self):
        return self.name