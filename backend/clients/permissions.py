from rest_framework import permissions

class IsCompanyUser(permissions.BasePermission):
    """
    Permite acesso apenas a usuários que pertencem a uma empresa.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.company is not None

    def has_object_permission(self, request, view, obj):
        # Garante que o usuário só pode acessar clientes da sua empresa
        return obj.company == request.user.company
