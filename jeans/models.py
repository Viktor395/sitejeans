
from tabnanny import verbose
from django.db import models

class Jeans(models.Model):
    title = models.CharField('Назва джинсів', max_length=100)
    text = models.TextField('Опис джинсів')

    def __str__(self):
        return 'Джинси жіночі'
        

    class Meta:
        verbose_name = 'ДЖИНСИ'
            
        
