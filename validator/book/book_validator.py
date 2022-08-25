

from distutils.log import error
from sys import flags
import datetime
import threading
from threading import Thread

class BookGenreVlidator(threading.Thread):
    list_of_errors = []
    flag = True

    def __init__(self , model) -> None:
        threading.Thread.__init__(self)
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
       #domain will be resolved on first thread
       self.resolve_domain()
       #thumbnail will be resolved on second OR newly created below thread
       thread2 = Thread(target=self.generate_website_thumbnail)
       thread.start()
       # thread1 will wait for thread2
       self.join()
       # thread2 will wait for thread1, if it's late.
       thread2.join()
       # here it will print ip and thumbnail before exiting first thread
       print(self.domain_ip, self.website_thumbnail)



class BookClassValidator(threading.Thread):
    list_of_errors = []
    flag = True

    def __init__(self , model , genre_model) -> None:
        threading.Thread.__init__(self)
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
    def run(self):
       #domain will be resolved on first thread
       self.resolve_domain()
       #thumbnail will be resolved on second OR newly created below thread
       thread2 = Thread(target=self.generate_website_thumbnail)
       thread.start()
       # thread1 will wait for thread2
       self.join()
       # thread2 will wait for thread1, if it's late.
       thread2.join()
       # here it will print ip and thumbnail before exiting first thread
       print(self.domain_ip, self.website_thumbnail)


class BookObjectValidator(threading.Thread):
    list_of_errors = []
    flag = True

    def __init__(self , model , class_model) -> None:
        threading.Thread.__init__(self)
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

    def run(self):
       #domain will be resolved on first thread
       self.resolve_domain()
       #thumbnail will be resolved on second OR newly created below thread
       thread2 = Thread(target=self.generate_website_thumbnail)
       thread.start()
       # thread1 will wait for thread2
       self.join()
       # thread2 will wait for thread1, if it's late.
       thread2.join()
       # here it will print ip and thumbnail before exiting first thread
       print(self.domain_ip, self.website_thumbnail)


class BookBasketValidator(threading.Thread):
    flag = True
    list_of_errors = []

    def __init__(self , model) -> None:
        threading.Thread.__init__(self)
        self.model = model

    def is_valid(self , obj):
        if not self.model.objects.filter(code = obj).exists():

            self.flag = False

            return "this book with the given code doesn't exists in database!"
    def run(self):
       #domain will be resolved on first thread
       self.resolve_domain()
       #thumbnail will be resolved on second OR newly created below thread
       thread2 = Thread(target=self.generate_website_thumbnail)
       thread.start()
       # thread1 will wait for thread2
       self.join()
       # thread2 will wait for thread1, if it's late.
       thread2.join()
       # here it will print ip and thumbnail before exiting first thread
       print(self.domain_ip, self.website_thumbnail)
