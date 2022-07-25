from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Empresa
import json


# Create your views here.
class EmpresaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if( id > 0):
            empresas = list(Empresa.objects.filter(id=id).values())
            if len(empresas) > 0:
                empresa = empresas[0]
                datos = {'message':"Success", 'empresas':empresa}
            else:
                datos = {'message':"Empresas not found..."}
            return JsonResponse(datos)
        else:     
            empresas = list(Empresa.objects.values())
            if len(empresas) > 0:
                datos = {'message':"Success", 'empresas':empresas}
            else :
                datos = {'message':"Empresas not found..."}
            return JsonResponse(datos)

    def post(self, request):
        jdata = json.loads(request.body)
        Empresa.objects.create(nombre_empresa=jdata['nombre_empresa'], direccion=jdata['direccion'], 
        nit=jdata['nit'], telefono=jdata['telefono'])
        datos = {'message':"Succes"}
        return JsonResponse(datos)

    def put(self, request, id):
        jdata = json.loads(request.body)
        empresas = list(Empresa.objects.filter(id=id).values())
        if len(empresas) > 0:
            empresa = Empresa.objects.get(id=id)
            empresa.nombre_empresa = jdata['nombre_empresa']
            empresa.direccion = jdata['direccion']
            empresa.nit = jdata['nit']
            empresa.telefono = jdata['telefono']
            empresa.save()
            datos = {'message':"Succes"}
        else:
            datos = {'message':"Empresas not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        empresas = list(Empresa.objects.filter(id=id).values())
        if len(empresas) > 0:
            Empresa.objects.filter(id=id).delete()
            datos = {'message':"Succes"}
        else:
            datos = {'message':"Empresas not found..."}
        return JsonResponse(datos)
        

