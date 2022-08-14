from rest_framework import permissions


class IsActive(permissions.BasePermission):

    

    def has_permission(self, request, view):
        if request.user.admin_is_active == True:
            
            
            return True
      
        return False

   