from django.conf.urls import url
from .views import TelefoneListView, TelefoneCreateView, TelefoneUpdateView, TelefoneDeleteView
#from .views import EditalUpdateView, EditalDeleteView

urlpatterns = [
    url(r'list/$', TelefoneListView.as_view(), name='telefone_list'),
    url(r'cad/$', TelefoneCreateView.as_view(), name='telefone_create'),
    url(r'(?P<pk>\d+)/$', TelefoneUpdateView.as_view(), name='telefone_update'),
    url(r'(?P<pk>\d+)/delete/$', TelefoneDeleteView.as_view(), name='telefone_delete'),
]
