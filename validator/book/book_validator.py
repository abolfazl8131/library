from sys import flags
import datetime
import threading
from threading import Thread

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
        
    def run(self):
        t1 = threading.Thread(target=self.isvalid)
        
        t1.start()
        
        t1.join()
        



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

        
        if self.model.objects.filter(name = book_class).exists():
            self.flag = False
            self.list_of_errors.append("this class hase been set so far! try another...")
            
        if not self.genre_model.objects.filter(genre= genre).exists():
            self.flag = False
            self.list_of_errors.append("this genre does not exist in database....")


        if self.flag == False:
            return self.list_of_errors
        return True
        
    def run(self):
        t1 = threading.Thread(target=self.isvalid)
        
        t1.start()
       
        t1.join()
      


class BookObjectValidator:
    list_of_errors = []
    flag = True

    def __init__(self , model , class_model) -> None:
        
        self.model = model
        self.class_model = class_model

    def isvalid(self , code , book_class , date_published , published_no):
        
        self.class_validator(book_class)
        self.code_validator(code)
        self.date_validator(date_published)
        self.published_no_validator(published_no)

        if self.flag == False:
            return self.list_of_errors
        return True
        
    def code_validator(self , code):
         
        if isinstance(code , str) == False:
            self.flag = False
            self.list_of_errors.append("the code format must be string!")

    def published_no_validator(self , published_no):
        
        if isinstance(published_no , int) == False:
            self.flag = False
            self.list_of_errors.append("published number format must be integer")
 
    def date_validator(self , date_published):
        try:
            datetime.datetime.strptime(date_published, '%Y-%m-%d')
        except ValueError:
            self.flag = False
            self.list_of_errors.append("Incorrect date format, should be YYYY-MM-DD")

    def class_validator(self , book_class):
        if not self.class_model.objects.filter(name= book_class).exists():
            self.flag = False
            self.list_of_errors.append("this book class doesn't exist in data base first insert book class!")
    

    def run(self):
        t1 = threading.Thread(target=self.isvalid)
        t2 = threading.Thread(target=self.date_validator)
        t3 = threading.Thread(target=self.code_validator)
        t4 = threading.Thread(target=self.published_no_validator)
        t5 = threading.Thread(target=self.class_validator)

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        

        


class BookBasketValidator:
    flag = True
    list_of_errors = []

    def __init__(self , model) -> None:
        
        self.model = model

    def is_valid(self , obj):
        if not self.model.objects.filter(code = obj).exists():

            self.flag = False

            return "this book with the given code doesn't exists in database!"
            
    def run(self):
        t1 = threading.Thread(target=self.is_valid)
      
        t1.start()
        
        t1.join()
        