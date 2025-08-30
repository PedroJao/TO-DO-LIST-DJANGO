from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import TarefaForm
from .models import Tarefa
import json
from datetime import datetime
from django.http import JsonResponse
# Create your views here.

def adicionar_tarefas(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'adicionar_tarefas.html', {'form': form})

def ver_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'ver_tarefas.html', {'tarefas': tarefas})

def atualizar_tarefas(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('ver_tarefas')
    else:
        form = TarefaForm(instance=tarefa)

def editar_tarefas(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    form = TarefaForm(instance=tarefa)
    return render(request, 'editar_tarefas.html', {'form': form, 'tarefa': tarefa})

def deletar_tarefas(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('ver_tarefas')


@csrf_exempt
def atualizar_status(request, id):
    if request.method == "POST":
        dados = json.loads(request.body)
        try:
            tarefa = Tarefa.objects.get(pk=id)
            tarefa.concluida = dados.get("concluida", False)
            if tarefa.concluida:
                tarefa.data_conclusao = datetime.now()
            else:
                tarefa.data_conclusao = None
            tarefa.save()
            return JsonResponse({"sucesso": True})
        except Tarefa.DoesNotExist:
            return JsonResponse({"erro": "Tarefa não encontrada"}, status=404)