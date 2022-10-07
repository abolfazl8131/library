from rest_framework import permissions
from management.models import LibraryAdmin
class UnAuthorized(Exception):

    pass
        

class IsCompanyOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        
        try:

            return True
        
        except:

            raise UnAuthorized("please login!")

  
