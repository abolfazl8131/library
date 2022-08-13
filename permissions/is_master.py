from rest_framework import permissions


class IsMaster(permissions.BasePermission):

    

    def has_permission(self, request, view):
        if request.user.admin_position:
            return True
        
        return False
