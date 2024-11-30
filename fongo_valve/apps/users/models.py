from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomerUser(AbstractUser):
    ROLE_CHOICIES = [
        ('student','Etudiant'),
        ('admin','Admin '),
        ('club_student','Club student')
    ]

    roles = models.CharField(max_length=50, choices=ROLE_CHOICIES, default='student')
    departement = models.CharField(max_length=50 ,blank=True , null=True)

    def __str__(self):
        return f"{self.username}, {self.roles}"



