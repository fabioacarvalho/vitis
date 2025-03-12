from rest_framework import permissions


class HasCompanyAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.company is not None
    
    def has_object_permission(self, request, view, obj):
        return obj.company == request.user.company


class IsCompanyAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_company_admin and request.user.company is not None
