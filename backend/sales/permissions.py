from rest_framework import permissions

class IsCompanyUser(permissions.BasePermission):
    """
    Permite acesso apenas a usuários que pertencem a uma empresa.
    """

    def has_permission(self, request, view):
        # Garante que o usuário está autenticado e pertence a uma empresa
        return request.user.is_authenticated and request.user.company is not None

    def has_object_permission(self, request, view, obj):
        # Garante que o usuário só pode acessar dados da sua própria empresa
        return obj.company == request.user.company

class IsDealOwner(permissions.BasePermission):
    """
    Permite acesso apenas ao usuário responsável pelo deal.
    """

    def has_object_permission(self, request, view, obj):
        # Garantir que o usuário só possa acessar os deals que ele é responsável
        return obj.lead.company == request.user.company

class IsLeadOwner(permissions.BasePermission):
    """
    Permite acesso apenas ao usuário responsável pelo lead.
    """

    def has_object_permission(self, request, view, obj):
        # Garantir que o usuário só possa acessar os leads que ele é responsável
        return obj.company == request.user.company
