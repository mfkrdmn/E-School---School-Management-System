from django.db import models

# Create your models here.
class Classes(models.Model):
    
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name