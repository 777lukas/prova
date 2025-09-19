from django.shortcuts import render

# Create your views here.

from .models import Tarefa
# from django.http import HttpResponse

# def listar_tarefas(request):
#     tarefas_salvas = Tarefa.objects.all()
#     print(tarefas_salvas)
#     return HttpResponse("View 'listar_tarefas' executada! Confira no terminal")


def listar_tarefas(request):
    # 1. a busca no banco de dados continua a mesma
    tarefas_salvas = Tarefa.objects.all()
    #2. criamos um "dicionario do contexto" para enviar os dados ao template.
    # A chave 'minhas_tarefas' sera a variavel que usarmos no HTML.
    contexto = {
        'minhas_tarefas' : tarefas_salvas
    }
    #3. redenrizarmos o template, passando a requisição e o contexto com os dados.
    return render(request, 'tarefas/lista/lista.html', contexto)
