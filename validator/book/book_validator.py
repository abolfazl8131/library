

from distutils.log import error
from sys import flags
import datetime

class BookGenreVlidator:
    list_of_errors = []
    flag = True

    def __init__(self , model) -> None:
        self.model = model


    def isvalid(self, genre):
        if genre.isalpha() == False:
           
            self.flag = False
            self.list_of_errors.append("genre must be alpha! don't add numerical or other values.")

        
        if self.model.objects.filter(genre = genre).exists():
            self.list_of_errors.append("this genre hase been set so far! try another...")
            self.flag = False
        
        
        if self.flag == False:
            return self.list_of_errors
        return True



class BookClassValidator:
    list_of_errors = []
    flag = True

    def __init__(self , model , genre_model) -> None:
        self.model = model
        self.genre_model = genre_model

    def isvalid(self , book_class , genre):
        if isinstance(book_class , str) == False:
           
            self.flag = False
            self.list_of_errors.append("name must be alpha! don't add numerical or other values.")

        
        if self.model.objects.filter(name= book_class).exists():
            self.flag = False
            self.list_of_errors.append("this class hase been set so far! try another...")
            
        if not self.genre_model.objects.filter(genre= genre).exists():
            self.flag = False
            self.list_of_errors.append("this genre does not exist in database....")


        if self.flag == False:
            return self.list_of_errors
        return True


class BookObjectValidator:
    list_of_errors = []
    flag = True

    def __init__(self , model , class_model) -> None:
        self.model = model
        self.class_model = class_model

    def isvalid(self , code , book_class , date_published , published_no):
        
        if not self.class_model.objects.filter(name= book_class).exists():
            self.flag = False
            self.list_of_errors.append("this book class doesn't exixt in data base first insert book class!")
        
        try:
            datetime.datetime.strptime(date_published, '%Y-%m-%d')
        except ValueError:
            self.flag = False
            self.list_of_errors.append("Incorrect date format, should be YYYY-MM-DD")
        
        if isinstance(code , str) == False:
            self.flag = False
            self.list_of_errors.append("the code format must be string!")

        if isinstance(published_no , int) == False:
            self.flag = False
            self.list_of_errors.append("published number format must be integer")


        if self.flag == False:
            return self.list_of_errors
        return True
