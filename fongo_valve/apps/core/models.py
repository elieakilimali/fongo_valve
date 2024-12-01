from django.db import models

class BaseModel(models.Model):
    """
    Modèle de base avec des champs de suivi temporel
    """
    created_at = models.DateTimeField(auto_now_add=True , blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True , blank=True,null=True)

    class Meta:
        abstract = True  

