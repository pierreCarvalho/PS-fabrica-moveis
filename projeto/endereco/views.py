from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Endereco
from django.contrib import messages


# Create your views here.
class EnderecoListView(ListView):
    model = Endereco

class EnderecoCreateView(CreateView):
    model = Endereco
    fields = ['rua','numero', 'cep','bairro']
    success_url = 'endereco_list'

class EnderecoUpdateView(UpdateView):
    model = Endereco
    fields = ['rua','numero', 'cep','bairro']
    success_url = 'endereco_list'

class EnderecoDeleteView(DeleteView):
    model = Endereco
    success_url = 'endereco_list'

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
            messages.error(request, 'Há dependências ligadas à esse telefone, permissão negada!')
        return redirect(self.success_url)
