import os
import jwt
from customer.models import Customer
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from management.models import LibraryAdmin


def set_library_admin():
    pass


class AdminMiddleWare(MiddlewareMixin):

    WHITELISTED_URLS = ['/admin/save/',
    '/management/admin/update/' ,
    '/management/admin/delete/',
    '/management/admin/deactivate/' ,
    '/management/admin/activate/' , 
    '/management/admin/all/' ,
    '/management/admin/leave/' ,
    '/management/admin/query/',
    '/management/over-all-customer-views/' ,
    '/management/query-customer/' ,
    #'/management/profile/'
    ]

    def process_request(self, request):
        
        if request.path in self.WHITELISTED_URLS:
            user = request.user

            print(user)
            
            try:
                management = LibraryAdmin.objects.get(id = user.id)
                
                request.library_admin = management

                print(request.library_admin)

            except Exception as e:
                print(e)
                return JsonResponse({'error':'jwt expired!'} , status = 401)
        else:
            pass

            

    
            
