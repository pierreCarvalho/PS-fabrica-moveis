from django.conf.urls import url
from .views import TelefoneListView, TelefoneCreateView
#from .views import EditalUpdateView, EditalDeleteView

urlpatterns = [
    url(r'telefone/list/$', TelefoneListView.as_view(), name='telefone_list'),
    url(r'telefone/cad/$', TelefoneCreateView.as_view(), name='telefone_create'),
    #url(r'(?P<pk>\d+)/$', EditalUpdateView.as_view(), name='edital_update'),
    #url(r'(?P<pk>\d+)/delete/$', EditalDeleteView.as_view(), name='edital_delete'),
]
