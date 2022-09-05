from django.http import Http404

class BookBasket:
   
    def __init__(self , book_model , basket , customer) -> None:
        self.book_model = book_model
        self.basket = basket
        self.customer = customer

    def get_book_object(self , book_object , available:bool):
        return self.book_model.objects.get(code = book_object , available = available)

    def add(self , book_object):
        try:
            m = self.get_book_object(book_object , True)
            
            self.basket.objects.create(book_object = m , customer = self.customer)

        except Exception as e:
            
            raise Http404

    def get(self):
        return self.basket.objects.filter(customer = self.customer)

    def delete_obj(self , book_object):
        try:
            obj = self.get_book_object(book_object , False)
            self.basket.objects.get(customer = self.customer , book_object = obj).delete()
            
        except Exception as e:
            raise Http404


    def delete(self):
        self.basket.objects.filter(customer = self.customer).delete()

   


    

