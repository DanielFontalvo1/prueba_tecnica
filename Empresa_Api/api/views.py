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
    
    def verificarNit(self, nit):
        empresa = list(Empresa.objects.filter(nit=nit).values())
        if len(empresa) > 0:
            return False
        return True

    #metodo get que permite traer todos los registro o solo uno
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

    #Metodo postque permite registrar una empresa
    def post(self, request):

        jdata = json.loads(request.body)
        if(self.verificarNit(jdata['nit'])):
            Empresa.objects.create(nombre_empresa=jdata['nombre_empresa'], direccion=jdata['direccion'], 
            nit=jdata['nit'], telefono=jdata['telefono'])
            datos = {'message':"Succes"}
            return JsonResponse(datos)
        datos = {'message':"No Succes"}
        return JsonResponse(datos)

    #Metodo put que permite actualizar un registro
    def put(self, request, id):
        jdata = json.loads(request.body)
        empresas = list(Empresa.objects.filter(id=id).values())
        
        if (len(empresas) > 0):
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

    #Metodo delete para eliminar un registro, recibe un id para poder eliminar este id en especifico
    def delete(self, request, id):
        empresas = list(Empresa.objects.filter(id=id).values())
        if len(empresas) > 0:
            Empresa.objects.filter(id=id).delete()
            datos = {'message':"Succes"}
        else:
            datos = {'message':"Empresas not found..."}
        return JsonResponse(datos)

    


