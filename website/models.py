from django.db import models

from tinymce.models import HTMLField

class Base(models.Model):
     date_create = models.DateField( auto_now_add=True)
     date_update = models.DateField(auto_now=True )
     status = models.BooleanField(default=True)

     class Meta:

         abstract = True


class Banner(Base):
    title = HTMLField()
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.title

    class Meta :
        verbose_name= 'Banner'
        verbose_name_plural= 'Banners'



class About(Base):
    description = HTMLField()
    image = models.FileField(upload_to='images')

    def __str__(self):
        return f'self.image'

    class Meta :
        verbose_name= 'About'
        verbose_name_plural= 'Abouts'

    
class Configuration(Base):
    entete_about = HTMLField()
    entete_service = HTMLField()
    entete_portfolio = HTMLField()
    entete_contact = HTMLField()
    copyright = models.CharField(max_length=250)

    class Meta :
        verbose_name= 'Configuration'
        verbose_name_plural= 'Configurations'


class Website(Base):
    nom_site = models.CharField(max_length=250)
    logo_site = models.FileField(upload_to='images')
    phone = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    


    def __str__(self):
        return self.nom_site

    class Meta :
        verbose_name= 'Website'
        verbose_name_plural= 'Websites'


class Stat(Base):
    statistique = models.CharField(max_length=250)
    nom_statistique = models.CharField(max_length=250)

    def __str__(self):
        return self.nom_statistique

    class Meta :
        verbose_name= 'Stat'
        verbose_name_plural= 'Stats'



    
# Create your models here.
