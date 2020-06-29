
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fornecedor
from django.contrib import messages

class FornecedorListView(ListView):
    model = Fornecedor

class FornecedorCreateView(CreateView):
    model = Fornecedor
    fields = ['nome','cnpj', 'endereco','telefone']
    success_url = 'fornecedor/fornecedor_list'

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    fields = ['nome','cnpj', 'endereco','telefone']
    success_url = 'fornecedor/fornecedor_list'

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    success_url = 'fornecedor/fornecedor_list'
    
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse fornecedor, permissão negada!')
        return redirect(self.success_url)