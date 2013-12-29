from django.db import models

# Create your models here.


class TipoDeBaile(models.Model):
    name = models.CharField('Tipo de Baile',
                            max_length=20,
                            default='Salsa')
    def __unicode__(self):
        return self.name



class PasoDeBaile(models.Model):
    tipobaile = models.ForeignKey(TipoDeBaile)
    name = models.CharField(max_length=100,unique=True)
    video = models.URLField(blank=True,null = True)
    comment = models.TextField()
    pub_date = models.DateTimeField('Date Published',auto_now_add=True)
    def __unicode__(self):
        return self.name
    def has_video(self):
        if self.video:
            return True
        else:
            return False