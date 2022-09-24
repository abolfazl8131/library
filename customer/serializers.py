
from rest_framework import serializers


from customer.models import Customer


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['ID','first_name', 'last_name', 'birth_date','email','phone_number' , 'date_joined']
        extra_kwargs = {
            'email': {'write_only': True},
            'phone_number': {'write_only': True},
            'date_joined': {'read_only' : True}
        }


class GetCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['ID','first_name', 'last_name', 'birth_date','email','phone_number' , 'date_joined']
        

class UpdateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'birth_date','email','phone_number']
    
    def update(self, instance, validated_data):
       
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance

