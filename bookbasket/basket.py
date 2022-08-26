import threading

class BookBasket:
    book_objects = []

    def __init__(self) -> None:
        pass

    def add(self , book_object):
        self.book_objects.append(book_object)

    def get(self):
        return self.book_objects

    def run(self):
        t1 = threading.Thread(target=self.add)
        t2 = threading.Thread(target=self.get)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


    

