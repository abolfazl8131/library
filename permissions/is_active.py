from re import T
from rest_framework import permissions
from management.models import LibraryAdmin

class UnAuthorized(Exception):

    pass
        

class IsActive(permissions.BasePermission):

    

    def has_permission(self, request, view):
          
        try:
            
            user = request.user

            admin = LibraryAdmin.objects.get(id = user.id)

            if admin.is_active==True :
                
                return True
        
            return False

            

        except Exception as e:
            print(e)
            raise UnAuthorized("please login!")

   