from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.db.models import Q

from .forms import InspetorForm, RegistraVistoriaForm, VistoriaForm
from .models import Vistoria, VistoriaImage

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista-vistorias')  # Redireciona para a página inicial após o login
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def lista_vistorias(request):
    vistorias = Vistoria.objects.filter(esta_vistoriado=False)
    context = {'vistorias': vistorias}
    return render(request, 'list-vistorias.html', context)

def form_inspetor(request):
    form = InspetorForm() 
    if request.method == 'POST':
        form = InspetorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-vistorias')   
    return render(request, 'form-inspetor.html', {'form': form})

def form_vistoria(request):
    form = VistoriaForm()
    if request.method == 'POST':
        form = VistoriaForm(request.POST, request.FILES)
        if form.is_valid():
            vistoria = form.save()
            files = request.FILES.getlist('Vistoria') ## pega todas as imagens
            if files:
                for f in files:
                    VistoriaImage.objects.create( # cria instance para imagens
                        vistoria=vistoria, 
                        image=f
                    )
            return redirect('lista-vistorias')  
    return render(request, 'form-vistoria.html', {'form': form})

def form_registra_vistoria(request, id):
    get_registro = Vistoria.objects.get(id=id) ## pega objeto
    form = RegistraVistoriaForm()  
    if request.method == 'POST':
        form = RegistraVistoriaForm(request.POST)
        if form.is_valid():
            registro_form = form.save(commit=False)
            registro_form.vistoria = get_registro ## salva id da vistoria 
            registro_form.save() 
            ## muda status do imovel para "Alugado"
            get_registro.esta_vistoriado = True ## passa ser True
            get_registro.save() 
            return redirect('lista-vistorias') # Retorna para lista
    context = {'form': form, 'registro': get_registro}
    return render(request, 'form-registra-vistoria.html', context)

def reports(request):
    vistorias = Vistoria.objects.all() 
    inspetor = request.GET.get('inspetor')
    get_esta_vistoriado = request.GET.get('esta_vistoriado')
    get_tipo_item = request.GET.get('tipo_item')
    get_dt_inicio = request.GET.get('dt_inicio')
    get_dt_fim = request.GET.get('dt_fim')

    if inspetor:
        vistorias = vistorias.filter(
            Q(reg_vistoria__inspetor__nome__icontains=inspetor) |
            Q(reg_vistoria__inspetor__email__icontains=inspetor)
        )

    if get_esta_vistoriado is not None:
        vistorias = vistorias.filter(esta_vistoriado=get_esta_vistoriado)
    
    if get_tipo_item:
        vistorias = vistorias.filter(tipo_item=get_tipo_item)

    if get_dt_inicio and get_dt_fim:
        vistorias = vistorias.filter(reg_vistoria__create_at__range=[get_dt_inicio, get_dt_fim])




    return render(request, 'reports.html', {'vistorias': vistorias})
