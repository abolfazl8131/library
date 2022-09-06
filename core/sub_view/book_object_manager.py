from ..models import BookObject , Basket , LoanBook
class BOM_:
    def __init__(self) -> None:
        self.model = BookObject
        self.basket = Basket
        self.loan_book = LoanBook
    
    def save(self , loan_object , customer):
        try:
            book_objects = self.basket.objects.filter(customer = customer).values('book_object__code')

            
            for book_object in book_objects:

                code = book_object['book_object__code']

                book_object = self.model.objects.get(code = code)

                loan_book = self.loan_book.objects.create(loan = loan_object , book_object = book_object)

                loan_book.save()

            self.basket.objects.filter(customer = customer).delete()

        except Exception as e:
            raise e

    def availablity(self , data):
        try:
            loan_book_objects = self.loan_book.objects.filter(loan__id = data['id']).values('book_object__code')

            for loan_book_object in loan_book_objects:
                code = loan_book_object['book_object__code']
                book_obj = self.model.objects.get(code = code)
                book_obj.is_available()
                book_obj.save()     
            
        except Exception as e:
            raise e

    

        
