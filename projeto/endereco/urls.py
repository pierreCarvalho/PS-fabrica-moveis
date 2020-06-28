from django.conf.urls import url
from .views import EnderecoListView, EnderecoCreateView, EnderecoUpdateView, EnderecoDeleteView

urlpatterns = [
    url(r'list/$', EnderecoListView.as_view(), name='endereco_list'),
    url(r'cad/$', EnderecoCreateView.as_view(), name='endereco_create'),
    url(r'(?P<pk>\d+)/$', EnderecoUpdateView.as_view(), name='endereco_update'),
    url(r'(?P<pk>\d+)/delete/$', EnderecoDeleteView.as_view(), name='endereco_delete'),
]
