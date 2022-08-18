from rest_framework import permissions


class IsActive(permissions.BasePermission):

    

    def has_permission(self, request, view):
        try:
            if request.user.admin_is_active == True:
                
                
                return True
        
            return False
        except:
            return False

   