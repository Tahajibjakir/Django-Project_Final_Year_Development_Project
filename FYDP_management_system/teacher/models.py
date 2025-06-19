from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class T_Profile(models.Model):
    DESIGNATION=(
        ('PROFESSOR','PROFESSOR'),
        ('ASSISTANT PROFESSOR','ASSISTANT PROFESSOR'),
        ('LECTURER','LECTURER'),
        

    )

    EXPERTISE=(
        ('RESEARCH','RESEARCH'),
        ('THESIS','THESIS'),


    )

    

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    expertise=models.CharField(max_length=50, choices=EXPERTISE,null=True)
    designation=models.CharField(max_length=50, choices=DESIGNATION, null=True)
    
    phone=models.CharField(max_length=13)
    nationality=models.CharField(max_length=30)
    
    #profession=models.CharField(max_length=50, choices=CATEGORY, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
