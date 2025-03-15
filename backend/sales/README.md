Vamos criar o modelo de **Vendas**, que incluirá as entidades essenciais para o pipeline de vendas. Esses modelos ajudarão a gerenciar leads, negociações e a movimentação desses itens através das etapas do funil de vendas.

### 1. **Modelo Lead**:

Um **Lead** é um potencial cliente que ainda não se converteu em uma negociação formal. Podemos adicionar campos para rastrear o progresso do lead e informações importantes sobre ele.

```python
from django.db import models
from core.models import Company
from django.contrib.auth.models import User

class Lead(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Vendedor ou responsável pelo lead
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    status_choices = [
        ('new', 'Novo'),
        ('contacted', 'Contato Realizado'),
        ('qualified', 'Qualificado'),
        ('unqualified', 'Desqualificado'),
        ('converted', 'Convertido em Oportunidade'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.status}"

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
```

### 2. **Modelo Deal (Oportunidade)**:

O **Deal** é a negociação em andamento. Ele representa o estágio de conversão de um lead em uma oportunidade de venda.

```python
class Deal(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="deals")  # Referência ao Lead
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    stage_choices = [
        ('prospecting', 'Prospecção'),
        ('negotiation', 'Negociação'),
        ('closed_won', 'Fechado - Ganhou'),
        ('closed_lost', 'Fechado - Perdeu'),
    ]
    stage = models.CharField(max_length=20, choices=stage_choices, default='prospecting')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    expected_close_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.lead.name} - {self.stage}"

    class Meta:
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'
```

### 3. **Modelo Stage**:

O **Stage** define as etapas do funil de vendas. Cada oportunidade (deal) pode estar em um dos estágios definidos aqui.

```python
class Stage(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField()  # A ordem define onde esse estágio aparece no pipeline
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Stage'
        verbose_name_plural = 'Stages'
        ordering = ['order']
```

### 4. **Modelo Activity**:

A **Activity** representa interações com os leads ou clientes, como reuniões, telefonemas ou e-mails trocados.

```python
class Activity(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name="activities")
    activity_type_choices = [
        ('call', 'Chamada'),
        ('meeting', 'Reunião'),
        ('email', 'E-mail'),
        ('task', 'Tarefa'),
    ]
    activity_type = models.CharField(max_length=20, choices=activity_type_choices)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Quem realizou a atividade

    def __str__(self):
        return f"{self.activity_type} - {self.deal.lead.name}"

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
```

### 5. **Visões e Funcionalidades**:

Agora que temos os modelos, precisamos implementar as views para manipulação dos dados (listagem, criação, atualização e exclusão).

1. **Listagem de Leads**:
   - A visualização pode ser feita de forma simples para listar os leads de uma empresa.

2. **Criação e Edição de Deals**:
   - O processo de criação de oportunidades e o gerenciamento de suas etapas.

3. **Movimentação de Deals entre Estágios**:
   - Uma funcionalidade importante para permitir que um usuário mova oportunidades entre as fases do funil.

4. **Registro de Atividades**:
   - Para registrar interações como reuniões, chamadas ou e-mails trocados com o cliente.

### Como isso se encaixa na sua aplicação?

Esses modelos farão parte do seu módulo de vendas, permitindo a gestão dos leads, negociação, e movimentação pelo pipeline. Os dados desses modelos também vão interagir com a parte do marketing (para capturar leads) e o sucesso do cliente (para realizar atividades e follow-ups pós-venda).

<br>

## Explicando os Permissions:

**IsCompanyUser:** Este permission garante que o usuário só poderá acessar os dados que pertencem à sua empresa. <br>
**IsDealOwner:** Garante que o usuário só possa acessar e manipular deals que pertencem à sua empresa e que estão relacionados ao seu lead. <br>
**IsLeadOwner:** Garante que o usuário só possa acessar e manipular leads da sua empresa. <br>


