from rest_framework import permissions
from management.models import LibraryAdmin

class UnAuthorized(Exception):

    pass
        
class IsMaster(permissions.BasePermission):

    

    def has_permission(self, request, view):
        try:
            user = request.user
            admin = LibraryAdmin.objects.get(id = user.id)
            if admin.position== 'MS':
                
                return True
        
            return False

           
        except:
            raise UnAuthorized("please login!")
  
