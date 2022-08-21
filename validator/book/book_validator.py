

from distutils.log import error
from sys import flags


class BookVlidator:
    list_of_errors = []
    flag = True

    def __init__(self , model) -> None:
        self.model = model

    def class_isvalid(self , book_class):
        pass

    def genre_isvalid(self, genre):
        if genre.isalpha() == False:
            print("Ppp")
            self.flag = False
            self.list_of_errors.append("genre must be alpha! don't add numerical or other values.")

        
        if self.model.objects.filter(genre = genre).exists():
            self.list_of_errors.append("this genre hase been set so far! try another...")
            self.flag = False
        
        
        if self.flag == False:
            return self.list_of_errors
        return True




    def object_isvalid(self, **kwargs):
        pass
