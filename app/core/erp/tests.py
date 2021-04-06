from config.wsgi import *
from core.erp.models import Clientes

#Listar
#query = Clientes.objects.all()
#print(query)

#Agregar

#t = Clientes()
#t.nombres = 'Juan'
#t.apellidos = 'Perez Pinto'
#t.nro_documento = '123312313'
#t.save()

#editar
#t = Clientes.objects.get(id=2)
#t.nombres = 'Prueba de edición'
#t.save()
#print(t.nro_documento)

#eliminar
#t = Clientes.objects.get(id=3)
#t.delete()

#consulta avanzada los nombres que contenga la letra P
obj = Clientes.objects.filter(nombres__contains='P').count()
print(obj)