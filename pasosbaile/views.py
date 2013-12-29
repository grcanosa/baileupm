from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

from pasosbaile.models import PasoDeBaile,TipoDeBaile

def tipo_baile_index(request,dance_name):
    tipobaile_nombre = TipoDeBaile.objects.filter(name__iexact=dance_name)
    pasosbaile_list = PasoDeBaile.objects.filter(tipobaile__iexact=tipobaile_nombre)#.order_by('-name')[:5]
    context = {'dancestep_list': pasosbaile_list,'dancetype_name': tipobaile_nombre.first().name}
    return render(request, 'pasosbaile/baile_indice.html', context)

def paso_baile_detalle(request,dance_name,step_id):
    #tipobaile_nombre = TipoDeBaile.objects.filter(name__iexact=dance_name)
    paso_baile = PasoDeBaile.objects.filter(id=step_id)#.order_by('-name')[:5]
    if paso_baile:
        video_tag = paso_baile.first().video.split('/')[-1]
        context = {'paso_baile': paso_baile.first(),'video_tag':video_tag}
        return render(request, 'pasosbaile/detalle_paso.html', context)
    else:
        return render(request, 'pasosbaile/error.html')
    
def home(request):
    return render(request, 'pasosbaile/home.html')

def bailes_index(request):
    listabailes = TipoDeBaile.objects.all()
    context = {'listabailes':listabailes}
    return render(request, 'pasosbaile/lista_bailes.html',context)
