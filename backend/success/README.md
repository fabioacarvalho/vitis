## Explicação das Views:

1.	CustomerSuccessViewSet:
    •	Usa um ModelViewSet para fornecer CRUD completo para CustomerSuccess.
    •	Ação create: Cria um novo CustomerSuccess utilizando o serviço create_customer_success.
    •	Ação engagements: Retorna todos os Engagements relacionados a um CustomerSuccess.

2.	EngagementViewSet:
    •	Também um ModelViewSet para CRUD completo de Engagement.
    •	Ação create: Cria um novo Engagement e o associa a um CustomerSuccess e a um Lead.

3.	SupportTicketViewSet:
    •	ModelViewSet para CRUD de SupportTicket.
    •	Ação resolve: Permite resolver um SupportTicket passando a nota de resolução.
4.	TaskViewSet:
    •	ModelViewSet para CRUD de Task.
    •	Ação complete: Marca uma Task como concluída.
    
5.	CustomerFeedbackViewSet:
    •	ModelViewSet para CRUD de CustomerFeedback.
    •	Ação create: Cria um novo CustomerFeedback.