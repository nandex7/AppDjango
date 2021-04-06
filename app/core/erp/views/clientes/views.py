from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
 
from core.erp.forms import ClientesForm
from core.erp.models import Clientes

 
class ClientesView(ListView):
    model = Clientes
    template_name = 'clientes/list.html'

    #def get_queryset(self):
     #   return Clientes.objects.filter(nombres__startswith='P')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Clientes.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_tabla"] = 'LISTADO DE CLIENTES'
        context["titulo_pagina"] = 'Clientes'
        context["create_url"] = reverse_lazy('erp:clientes_create')
        return context

class ClientesCreateView(CreateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'clientes/create.html'
    success_url = reverse_lazy('erp:clientes_list')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print('accion ejecutadao: ' + action)
            if action == 'add':
                print('entro verdadero')
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_tabla"] = 'Nuevo Registro'
        context["titulo_pagina"] = 'Clientes'
        context["list_url_clientes"] = reverse_lazy('erp:clientes_list')
        context["action"] = 'add'
        return context

class ClientesUpdateView(UpdateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'clientes/create.html'
    success_url = reverse_lazy('erp:clientes_list')
 
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_tabla"] = 'Editar Registro'
        context["titulo_pagina"] = 'Clientes'
        context["list_url_clientes"] = reverse_lazy('erp:clientes_list')
        context["action"] = 'edit'
        return context

class ClientesDeleteView(DeleteView):

    model = Clientes
    template_name = 'clientes/delete.html'
    success_url = reverse_lazy('erp:clientes_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_tabla"] = 'Eliminar Registro'
        context["titulo_pagina"] = 'Clientes'
        context["list_url_clientes"] = reverse_lazy('erp:clientes_list')
        return context

class ClientesFormView(FormView):
    form_class = ClientesForm
    template_name = 'clientes/create.html'
    success_url = reverse_lazy('erp:clientes_list')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_tabla"] = 'Form | Clientes'
        context["titulo_pagina"] = 'Clientes'
        context["list_url_clientes"] = reverse_lazy('erp:clientes_list')
        context['action'] = 'add'
        return context