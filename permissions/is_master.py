from rest_framework import permissions


class IsMaster(permissions.BasePermission):

    

    def has_permission(self, request, view):
        if request.user.get_position()== 'MS':
            
            
            return True
      
        return False

  
