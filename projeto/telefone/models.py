from django.db import models
from django.db import connections
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
# Create your models here.
class Telefone(models.Model):
    
    numero = models.CharField(_(u'Numero do Telefone *'), max_length=100, help_text='Campo obrigatório como todos os que tiverem *')
    codigo_area = models.IntegerField('Códio Area *')
    descricao = models.CharField(_(u'Descrição *'),max_length=100)
    pessoa = models.CharField(_(u'Nome completo do contato'),max_length=100,blank=True)
    
    class Meta:
        db_table='Telefone'

    def __str__(self):
        return '%s - %s ' % (self.numero, self.descricao)

    def save(self, *args, **kwargs):
        super(Telefone, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('telefone_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('telefone_delete', args=[str(self.id)])