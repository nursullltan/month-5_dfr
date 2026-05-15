from django.db import models
import random
from django.contrib.auth.models import User

class UserConfirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="confirm_code")
    code = models.CharField(max_length=6)
    
    def __str__(self):
        return f"{self.user.username} - {self.code}"
    
    @staticmethod
    def generate_code():
        return str(random.randint(100000, 999999))
# Create your models here.
