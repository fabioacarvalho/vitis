# Vitis CRM

## Estrutura do Projeto

__Back-end:__ Django + DRF (para API REST)
__Banco de Dados:__ PostgreSQL (com multi-tenancy inicial simples – um único banco com empresa_id)
__Front-end:__ React (dashboard interativo)
__Autenticação:__ Django + JWT (para login seguro)
__Envio de e-mails:__ Celery + Redis (para automação básica e processamento em background)
__Hospedagem:__ AWS/GCP com Docker para deploy escalável

### Modulos

- __empresas/__ – Gerenciamento de empresas e usuários
- __vendas/__ – Pipeline de vendas e negociações
- __marketing/__ – Captura de leads e automação
- __sucesso_cliente/__ – Retenção e fidelização de clientes

