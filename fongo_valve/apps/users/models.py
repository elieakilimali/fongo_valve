from django.contrib.auth.models import AbstractUser
from django.db import models
from fongo_valve.apps.core.managers import UserManager
from fongo_valve.apps.core.models import BaseModel

class CustomerUser(AbstractUser,BaseModel):

    objects = UserManager()
    email = models.EmailField(unique=True)
    username = None 

    STUDENT = 'student'
    DEPARTMENT = 'department'
    CLUB = 'club'
    SUPER_ADMIN = 'super_admin'
    ROLE_CHOICES = [
        (STUDENT, 'Étudiant'),
        (DEPARTMENT, 'Département'),
        (CLUB, 'Club Étudiant'),
        (SUPER_ADMIN, 'Super Administrateur'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=STUDENT
    )


    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email

    def is_student(self):
        return self.role == self.STUDENT

    def is_department(self):
        return self.role == self.DEPARTMENT

    def is_club(self):
        return self.role == self.CLUB

    def is_super_admin(self):
        return self.role == self.SUPER_ADMIN
