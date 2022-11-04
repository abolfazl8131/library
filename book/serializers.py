
from rest_framework import serializers
from .models import BookObject, BookClass, BookGenre, BookImage

from company.serializers import CompanySerializer


class BookClassSerializer(serializers.ModelSerializer):

    genre = serializers.SlugRelatedField(queryset = BookGenre.objects.all() , slug_field='genre')
    image = serializers.FileField()
    class Meta:
        model = BookClass
        fields = ['name' , 'genre' , 'authors' , 'quantity','date_created','image']
        extra_kwargs = {
            'date_created': {'read_only': True}, 
        }
        
       
###################################################################################################################3
class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ['genre']


#########################################################################################################
class BookObjectSerializer(serializers.ModelSerializer):
    book_class = serializers.SlugRelatedField(queryset = BookClass.objects.all() , slug_field='name')
    class Meta:
        model = BookObject
        fields = ['code' , 'date_published' , 'published_no' , 'book_class' , 'company']


##############################################################################################



class NestedBookImageSerializer(serializers.ModelSerializer):
    image = serializers.FileField()
    class Meta:
        model = BookImage
        fields = ['image']


#######################################################################################################

class BookImageSerializer(serializers.ModelSerializer):

    book_object = serializers.SlugRelatedField(queryset = BookObject.objects.all() , slug_field='code')

    class Meta:

        model = BookImage

        fields = '__all__'

class BookClassNestedSerializer(serializers.ModelSerializer):
    genre = BookGenreSerializer()
    #image = BookImageSerializer()
    class Meta:
        model = BookClass
        fields = ['name' , 'genre' , 'authors']


class BookObjectGetSerializer(serializers.ModelSerializer):
    book_class = BookClassNestedSerializer()
    object_image = NestedBookImageSerializer(many = True)
    company = CompanySerializer()
    class Meta:
        model = BookObject
        fields = ['code' , 'date_published' , 'published_no' , 'book_class' , 'available','object_image' , 'company']

class BookClassGetSerializer(serializers.ModelSerializer):
    genre = BookGenreSerializer()
    #book_class = BookClassNestedSerializer()
    class Meta:
        model = BookClass
        fields = ['name' , 'genre' , 'authors' , 'quantity','date_created','image']  
        extra_kwargs = {
            'date_created': {'write_only': True}, 
        }     