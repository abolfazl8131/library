from rest_framework import permissions


class IsMaster(permissions.BasePermission):

    

    def has_permission(self, request, view):
        if request.user.get_position()== 'MS':
            
            print(request.user.get_position())
            return True
      
        return False

  
