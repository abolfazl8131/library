from rest_framework import permissions
from management.models import LibraryAdmin
class UnAuthorized(Exception):

    pass
        

class IsClerk(permissions.BasePermission):

    def has_permission(self, request, view):
        
        try:
            user = request.user
            admin = LibraryAdmin.objects.get(id = user.id)
            if admin.position== 'CL':
                
                return True
        
            return False

           
        except:
            raise UnAuthorized("please login!")

  
