from django.db import models
from django.db import connections
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from endereco.models import Endereco
from telefone.models import Telefone


# Create your models here.
class Fornecedor(models.Model):
    
    nome = models.CharField(_(u'Nome*'), max_length=100, help_text='Campo obrigatório como todos os que tiverem *')
    cnpj = models.CharField(_('CNPJ'),max_length=14, blank=True, null=True, help_text='Atenção: SOMENTE OS NÚMEROS')
    endereco = models.ForeignKey('endereco.Endereco', verbose_name="Endereço", null=True, blank=True, on_delete=models.PROTECT)
    telefone = models.ForeignKey('telefone.Telefone', verbose_name="Telefone", null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        db_table='Fornecedor'

    def __str__(self):
        return '%s' % (self.nome)

    def save(self, *args, **kwargs):
        super(Fornecedor, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('fornecedor_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('fornecedor_delete', args=[str(self.id)])