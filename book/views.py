
from django.http import JsonResponse
from requests import request
from rest_framework.views import APIView
from validator.book.book_validator import BookObjectValidator ,BookClassValidator , BookGenreVlidator
from .models import BookGenre ,BookClass , BookObject
from rest_framework.generics import DestroyAPIView, ListAPIView , CreateAPIView
from .serializers import BookClassGetSerializer , BookClassSerializer , BookObjectGetSerializer , BookObjectSerializer , BookGenreSerializer, BookImageSerializer
from shared_queries.get_all_objects import GetManagementObjects 
from permissions.is_active import IsActive
from permissions.is_clerk import IsClerk
from permissions.is_master import IsMaster
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.decorators.cache import cache_page

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL')
permissons = [IsActive , IsClerk | IsActive , IsMaster]

class GenreRegister(APIView):

    permission_classes = permissons
    serializer_class = BookGenreSerializer

    def post(self , format = None):
        
        data = self.request.data
        
        genre = data['genre']

        validator = BookGenreVlidator(BookGenre)

        validator.run()

        is_valid = validator.isvalid(genre)

        if not is_valid == True:

            return JsonResponse({"error":is_valid} , status = 400)

        serializer = self.serializer_class(data = data)
        
        serializer.is_valid(raise_exception=True)

        serializer.save()

        print(serializer.data)

        return JsonResponse({"data":serializer.data})

#update this class..................
class GenreFilter(ListAPIView):
    
    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    lookup_field = 'genre'




class DeleteGenre(DestroyAPIView):
   
    permission_classes = permissons

    def get_object(self , **kwargs):
        return BookGenre.objects.get(**kwargs)

    def delete(self , request):
        try:
            genre = request.GET.get('genre')
            qs = self.get_object(genre = genre)
            qs.delete()
            return JsonResponse({"msg":"deleted!"}, status = 400)
        except:
            return JsonResponse({"error":"we cant delete this genre because the is a hard relation bitween thid genre and some book classes!"} , status = 400)
        
###############################################################################################################################################

class ClassRegister(APIView):
    permission_classes = permissons
    serializer_class = BookClassSerializer

    #add

    def post(self , format = None):
        try:
            data = self.request.data

            validator = BookClassValidator(BookClass , BookGenre)
            validator.run()

            
            is_valid = validator.isvalid(data['name'] , data['genre'])

            if not is_valid == True:

                return JsonResponse({"error":is_valid}, status = 400)

            serializer = self.serializer_class(data = data)
            serializer.is_valid()
            serializer.save()
            return JsonResponse(serializer.data)
        except Exception as e: 
            raise e

    


class GetBookClasses(ListAPIView):
    serializer_class = BookClassGetSerializer

    def get_queryset(self , genre):
        qs = BookClass.objects.filter(genre__genre = genre)
        
        return qs

    @method_decorator(cache_page(CACHE_TTL))
    def get(self , request):
        genre = request.GET.get('genre')
        if not genre == "":
            qs = self.get_queryset(genre)
            serializer = self.serializer_class(qs , many = True)
            return JsonResponse({"data":serializer.data})
        all_objects = BookClass.objects.all()

        serializer = self.serializer_class(all_objects , many = True)
        return JsonResponse({"data":serializer.data})
   


class ClassDelete(DestroyAPIView):
    permission_classes = permissons
    

    def get_object(self , **kwargs):
        return BookClass.objects.get(**kwargs)

    def delete(self , request):
        try:
            name = request.GET.get('name')
            qs = self.get_object(name = name )
            qs.delete()
            return JsonResponse({"msg":"deleted!"})
        except:
            return JsonResponse({"error":"we cant delete this class because the is a hard relation between this class and some book objects!"} , status = 400)
##########################################################################################################################3
from shared_queries.lib_admin_middleware import find_library_admin
class ObjectRegister(APIView):
    serializer_class = BookObjectSerializer
    permission_classes = permissons

    def post(self , format = None):
        try:
            data = self.request.data

            validator = BookObjectValidator(BookObject , BookClass)
            validator.run()
            
            is_valid = validator.isvalid(data['code'] , data['book_class'] , data['date_published'] , data['published_no'])

           
            
            data['company'] =  find_library_admin(self.request.user.id).company.id

            if not is_valid == True:

                return JsonResponse({"error":is_valid}, status = 400)

            serializer = self.serializer_class(data = data)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            return JsonResponse({"data":serializer.data})
        except Exception as e:
            raise e


class GetBookObjectsWithSlug(ListAPIView):

    serializer_class = BookObjectGetSerializer
    
    model = BookObject

    def get_queryset(self , **kwargs):
        
        name = kwargs['name']
        
        return self.model.objects.filter(book_class__name = name).prefetch_related('object_image')



    @method_decorator(cache_page(CACHE_TTL))
    def get(self , request , *args, **kwargs):
        name = self.kwargs['name']
        qs = self.get_queryset(name = name)
        
        serializer = self.serializer_class(qs , many = True)
        return JsonResponse({"data":serializer.data})
    
    



class ObjectDelete(DestroyAPIView):
    permission_classes = permissons
    

    def get_queryset(self , **kwargs):
        return BookObject.objects.get(**kwargs)

    def delete(self , request):
        
        code = request.GET.get('code')
        qs = self.get_queryset(code = code , company =  find_library_admin(self.request.user.id).company)
        qs.delete()
        return JsonResponse({"msg":"deleted!"})
       

###########################################################################################################################

class UploadImage(CreateAPIView):

    permission_classes = permissons

    serializer_class = BookImageSerializer

    def get_object(self , **kwargs):

        obj = BookObject.objects.get(**kwargs)
        return obj

    def post(self, request):

        data = request.data

        data['book_object'] = self.get_object(code = data['book_object'] , company = self.request.user.company)

        serializer = self.serializer_class(data = data)

        serializer.is_valid(raise_exception= True)

        serializer.save()

        return JsonResponse(serializer.data)


