from django.db import models
from django.db import connections
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.
class Endereco(models.Model):

    rua = models.CharField(_(u'Rua *'), max_length=100, help_text='Campo obrigatório como todos os que tiverem *')
    numero = models.CharField('Numero *', max_length=20)
    cep = models.CharField(_(u'CEP *'),max_length=100)
    bairro =  models.CharField(_(u'Bairro *'), max_length=100, help_text='Campo obrigatório como todos os que tiverem *')
    
    class Meta:
        db_table='Endereco'
    
    def __str__(self):
        return '%s - %s ' % (self.rua, self.cep)

    def save(self, *args, **kwargs):
        super(Endereco, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('endereco_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('endereco_delete', args=[str(self.id)])