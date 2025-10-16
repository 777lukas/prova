from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto
from django.http import HttpResponse

def listar_projetos(request):
   
    projetos_salvos = Projeto.objects.all()
    
    
    contexto = {
        'meus_projetos': projetos_salvos 
    }

    return render(request, 'projetos/lista.html', contexto)

def detalhe_projeto(request, projeto_id):
    
    projeto = get_object_or_404(Projeto, pk=projeto_id)

    return render(request, 'projetos/detalhe.html', {'projeto': projeto})

def adicionar_projeto(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Projeto.objects.create(titulo=titulo, descricao=descricao)
        return redirect('lista_projetos')

    return render(request, 'projetos/form_projeto.html')



def alterar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        concluido = request.POST.get('concluido') == 'on' 

        projeto.titulo = titulo
        projeto.descricao = descricao
        projeto.concluido = concluido
        
        projeto.save()
        
        return redirect('lista_projetos')

    context = {
        'projeto': projeto,
    }
    return render(request, 'projetos/form_projeto.html', context)

def excluir_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    
    if request.method == 'POST':
        projeto.delete()
        return redirect('lista_projetos')
    
    return render(request, 'projetos/confirmar_exclusao.html', {'projeto': projeto})