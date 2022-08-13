from rest_framework import permissions


class IsMaster(permissions.BasePermission):

    

    def has_permission(self, request, view):
        if request.user.get_position()== 'MS':
            
            print(request.user.get_position())
            return True
      
        return False

    def has_object_permission(self, request, view, obj):
        if obj.get_position() == 'MS' and request.user.ID != obj.ID:

            print(obj.get_position())
            return False
            
        print("GDRTH")
        print(obj.get_position())
        return True
