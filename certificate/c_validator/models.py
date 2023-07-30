from django.db import models
from django.contrib.auth.models import User

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Certificate belongs to a specific user
    created_at = models.DateTimeField(auto_now_add=True)
    signature = models.CharField(max_length=30,blank=True,null=True)


    def __str__(self):
        return self.title

# Create your models here.
