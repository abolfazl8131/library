from rest_framework import permissions


class IsClerk(permissions.BasePermission):

    

    def has_permission(self, request, view):

        if request.user.get_position()== 'CL':
            
            return True
      
        return False

  
