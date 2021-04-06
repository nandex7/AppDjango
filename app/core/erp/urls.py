from django.urls import path
from core.erp.views.clientes.views import *
from core.erp.views.dashboard.views import *
app_name = 'erp'

urlpatterns = [
    #Clientes
    path('clientes/list/', ClientesView.as_view(), name='clientes_list'),
    path('clientes/add/', ClientesCreateView.as_view(), name='clientes_create'),
    path('clientes/update/<int:pk>/', ClientesUpdateView.as_view(), name='clientes_update'),
    path('clientes/delete/<int:pk>/', ClientesDeleteView.as_view(), name='clientes_delete'),
    path('clientes/form/', ClientesFormView.as_view(), name='clientes_form'),
    #Home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]