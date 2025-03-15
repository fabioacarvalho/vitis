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


class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

