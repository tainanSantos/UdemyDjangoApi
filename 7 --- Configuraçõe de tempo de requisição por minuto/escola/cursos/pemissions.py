from rest_framework import  permissions

class EhSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):

        # se o usuário for super usuário então ele pode deletar
        # se não então ele não pode deletar
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True
