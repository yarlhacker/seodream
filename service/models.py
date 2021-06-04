from django.db import models

from tinymce.models import HTMLField
from website.models import Base



class Feature(Base):
    number = models.IntegerField()
    logo = models.CharField( max_length=50)
    nom = models.CharField( max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.nom

    class Meta :
        verbose_name= 'Feature'
        verbose_name_plural= 'Features'


class Categorie(Base):
  
    nom = models.CharField( max_length=50)
  
    def __str__(self):
        return self.nom

    class Meta :
        verbose_name= 'Categorie'
        verbose_name_plural= 'Categories'


class Portfolio(Base):
  
    nom = models.CharField( max_length=50)
    image = models.FileField(upload_to='images')
    categorie = models.ForeignKey("service.Categorie", verbose_name=("categorie"), on_delete=models.CASCADE ,related_name='categorieportfolio')
  
    def __str__(self):
        return self.nom

    class Meta :
        verbose_name= 'Portfolio'
        verbose_name_plural= 'Portfolios'


class Service(Base):

    logo = models.FileField(upload_to='images')
    nom = models.CharField( max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.nom

    class Meta :
        verbose_name= 'Service'
        verbose_name_plural= 'Services'


class Contact(Base):

    surnom = models.CharField( max_length=50)
    nom = models.CharField( max_length=50)
    sujet = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.nom

    class Meta :
        verbose_name= 'Contact'
        verbose_name_plural= 'Contacts'




# Create your models here.
