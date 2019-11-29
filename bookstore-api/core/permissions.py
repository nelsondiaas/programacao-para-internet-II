from rest_framework import permissions
from .models import *


class AdressPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        return False


class ClientPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        return False


class AdministratorPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            if Administrator.objects.get(email=request.user.email):
                return True
        except Administrator.DoesNotExist:
            return False
