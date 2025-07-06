from django.urls import path
from django.contrib import admin
from tarefas import views

urlpatterns = [
    path('', views.ver_tarefas, name='ver_tarefas'),
    path('adicionar_tarefas/', views.adicionar_tarefas, name='adicionar_tarefas'),
    path('atualizar_tarefas/<int:id>/', views.atualizar_tarefas, name='atualizar_tarefas'),
    path('editar_tarefas/<int:id>/', views.editar_tarefas, name='editar_tarefas'),
    path('deletar_tarefas/<int:id>/', views.deletar_tarefas, name='deletar_tarefas'),
    path('atualizar_status/<int:id>/', views.atualizar_status, name='atualizar_status'),
]
