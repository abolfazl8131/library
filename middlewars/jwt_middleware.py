import os
import jwt
from customer.models import Customer
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class JWTMiddleWare(MiddlewareMixin):

    WHITELISTED_URLS = [
        "/customer/profile/" ,
        "/customer/update/" , 
        "/core/basket/add/" , 
        "/core/basket/delete/" , 
        "/core/basket/get/" , 
        "/core/rent/save/"]

    def process_request(self, request):
        
        if request.path in self.WHITELISTED_URLS:
            token = request.META.get("HTTP_AUTHORIZATION", "")
            
            try:
                user_ID = jwt.decode(token , key = str(os.environ.get("SECRET_KEY")) , algorithms = ["HS256"])['ID']
                
                user_obj = Customer.objects.get(ID = user_ID)

                request.customer  = user_obj
                

            except Exception as e:
                
                return JsonResponse({'error':'jwt expired!'} , status = 401)
        else:
            pass

            

    
            
