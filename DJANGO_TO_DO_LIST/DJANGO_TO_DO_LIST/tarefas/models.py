from django.db import models

# Tabela de tarefas
class Tarefa(models.Model):
    # Cada tarefa tem um título, descrição, status de conclusão e datas de criação e conclusão
    id = models.AutoField(primary_key=True, unique=True)
    titulo = models.CharField(max_length=50) 
    descricao = models.TextField(blank=True, null=True, max_length=200) 
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(blank=True, null=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'tarefas' # Nome da tabela no banco de dados
        ordering = ['-data_criacao'] # Ordena as tarefas pela data de criação, do mais recente para o mais antigo


