
from django.http import JsonResponse
from rest_framework.views import APIView
from validator.book.book_validator import BookObjectValidator ,BookClassValidator , BookGenreVlidator
from .models import BookGenre ,BookClass , BookObject
from rest_framework.generics import DestroyAPIView, ListAPIView , CreateAPIView
from .serializers import BookClassGetSerializer , BookClassSerializer , BookObjectGetSerializer , BookObjectSerializer , BookGenreSerializer, BookImageSerializer
from shared_queries.get_all_objects import GetObjects 
from permissions.is_active import IsActive
from permissions.is_clerk import IsClerk
from permissions.is_master import IsMaster
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.decorators.cache import cache_page

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL')
permissons = (IsActive , IsClerk | IsActive , IsMaster)

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



class GenreFilter(ListAPIView):
    
    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    lookup_field = 'genre'




class DeleteGenre(DestroyAPIView):
    query_class = GetObjects(BookGenre)
    permission_classes = permissons
    def get_queryset(self , **kwargs):
        self.query_class.run()
        qs = self.query_class.get_object(**kwargs)
        return qs

    def delete(self , request):
        try:
            genre = request.GET.get('genre')
            qs = self.get_queryset(genre = genre)
            qs.delete()
            return JsonResponse({"msg":"deleted!"}, status = 400)
        except:
            return JsonResponse({"error":"we cant delete this genre because the is a hard relation bitween thid genre and some book classes!"} , status = 400)
        
###############################################################################################################################################

class ClassRegister(APIView):
    permission_classes = permissons
    serializer_class = BookClassSerializer

    def post(self , format = None):
        
        data = self.request.data

        validator = BookClassValidator(BookClass , BookGenre)
        validator.run()
        is_valid = validator.isvalid(data['name'] , data['genre'])

        if not is_valid == True:

            return JsonResponse({"error":is_valid}, status = 400)

        serializer = self.serializer_class(data = data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse({"data":serializer.data})


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
    query_class = GetObjects(BookClass)

    def get_queryset(self , **kwargs):
        self.query_class.run()
        qs = self.query_class.get_object(**kwargs)
        return qs

    def delete(self , request):
        try:
            name = request.GET.get('name')
            qs = self.get_queryset(name = name)
            qs.delete()
            return JsonResponse({"msg":"deleted!"})
        except:
            return JsonResponse({"error":"we cant delete this class because the is a hard relation between this class and some book objects!"} , status = 400)
##########################################################################################################################3

class ObjectRegister(APIView):
    serializer_class = BookObjectSerializer
    permission_classes = permissons

    def post(self , format = None):
        
        data = self.request.data

        validator = BookObjectValidator(BookObject , BookClass)
        validator.run()
        
        is_valid = validator.isvalid(data['code'] , data['book_class'] , data['date_published'] , data['published_no'])

        if not is_valid == True:

            return JsonResponse({"error":is_valid}, status = 400)

        serializer = self.serializer_class(data = data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse({"data":serializer.data})


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
    query_class = GetObjects(BookObject)

    def get_queryset(self , **kwargs):
        self.query_class.run()
        qs = self.query_class.get_object(**kwargs)
        return qs

    def delete(self , request):
        
        code = request.GET.get('code')
        qs = self.get_queryset(code = code)
        qs.delete()
        return JsonResponse({"msg":"deleted!"})
       

###########################################################################################################################

class UploadImage(CreateAPIView):
    serializer_class = BookImageSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data = data)
        serializer.is_valid(raise_exception= True)
        serializer.save()

        return JsonResponse(serializer.data)


