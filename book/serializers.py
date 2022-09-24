
from rest_framework import serializers
from .models import BookObject, BookClass, BookGenre, BookImage




class BookClassSerializer(serializers.ModelSerializer):

    genre = serializers.SlugRelatedField(queryset = BookGenre.objects.all() , slug_field='genre')
    
    class Meta:
        model = BookClass
        fields = ['name' , 'genre' , 'authors' , 'quantity']
       
###################################################################################################################3
class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ['genre']

class BookClassGetSerializer(serializers.ModelSerializer):
    genre = BookGenreSerializer()
    class Meta:
        model = BookClass
        fields = ['name' , 'genre' , 'authors' , 'quantity']

#########################################################################################################
class BookObjectSerializer(serializers.ModelSerializer):
    book_class = serializers.SlugRelatedField(queryset = BookClass.objects.all() , slug_field='name')
    class Meta:
        model = BookObject
        fields = ['code' , 'date_published' , 'published_no' , 'book_class']


##############################################################################################
class BookClassNestedSerializer(serializers.ModelSerializer):
    genre = BookGenreSerializer()
    class Meta:
        model = BookClass
        fields = ['name' , 'genre' , 'authors']


class NestedBookImageSerializer(serializers.ModelSerializer):
    image = serializers.FileField()
    class Meta:
        model = BookImage
        fields = ['image']


class BookObjectGetSerializer(serializers.ModelSerializer):
    book_class = BookClassNestedSerializer()
    object_image = NestedBookImageSerializer(many = True)
    class Meta:
        model = BookObject
        fields = ['code' , 'date_published' , 'published_no' , 'book_class' , 'available','object_image']


#######################################################################################################

class BookImageSerializer(serializers.ModelSerializer):
    book_object = serializers.SlugRelatedField(queryset = BookObject.objects.all() , slug_field='code')
    class Meta:
        model = BookImage
        fields = '__all__'