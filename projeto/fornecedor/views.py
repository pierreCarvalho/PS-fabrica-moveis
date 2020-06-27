from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Telefone
from django.contrib import messages

class TelefoneListView(ListView):
    model = Telefone

class TelefoneCreateView(CreateView):
    model = Telefone
    fields = ['numero','codigo_area', 'descricao']
    success_url = 'telefone/telefone_list'

'''
class EditalUpdateView(LoginRequiredMixin, UpdateView):
    model = Edital
    fields = ['numero','descricao', 'abertura', 'encerra']
    success_url = 'edital_list'


class EditalDeleteView(LoginRequiredMixin, DeleteView):
    model = Edital
    success_url = 'edital_list'

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
            messages.error(request, 'Há dependências ligadas à esse edital, permissão negada!')
        return redirect(self.success_url)
'''