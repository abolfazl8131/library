
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from .serializers import SignUpSerializer , UpdateCustomerSerializer
from authentication.OTP import OTP
from shared_queries.get_all_objects import GetObjects
from validator.signup_validators import SignUpValidator
from validator.update_customer_validator import UpdateCustomerValidator
from .models import Customer 
from django.db import transaction



class SignUp(CreateAPIView):
    serializer_class = SignUpSerializer

    @transaction.atomic()
    def post(self, request, *args, **kwargs):

            data = request.data
            validator = SignUpValidator(data)
            validator.run()
            validator.model = Customer
            validator.is_valid()
    
            serializer = self.serializer_class(data=data)
            serializer.is_valid()
            serializer.save()
            return JsonResponse(serializer.data)





class GetProfile(APIView):
    

    def get(self, request):

        
        return JsonResponse({
                'ID':request.customer.ID , 
                'firstname':request.customer.first_name , 
                'lastname':request.customer.last_name,
                'email':request.customer.email, 
                'phone':request.customer.phone_number,
                'birthdate':request.customer.birth_date,
                'date joined':request.customer.date_joined,})


class UpdateProfile(UpdateAPIView):
    serializer_class =  UpdateCustomerSerializer
    

    def get_queryset(self , **kwargs):
        query = GetObjects(Customer)
        query.start()
        return query.get_object(**kwargs)


    def patch(self , request):
        data = request.data
        ID = self.request.customer.ID
        validator = UpdateCustomerValidator(data)
        validator.start()
        validator.is_valid()
        serializer = self.serializer_class(self.get_queryset(ID = ID),data = data , partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return JsonResponse(serializer.data , status = 201)



