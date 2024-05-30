from django.db import models

class userinfo(models.Model):
    name=models.CharField(max_length=20,null=True)
    age=models.CharField(max_length=3,null=True)
    phone=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True)
    job=models.CharField(max_length=30,null=True)
    address=models.CharField(max_length=30,null=True)
    def __str__(self):
        return str(self.name)
