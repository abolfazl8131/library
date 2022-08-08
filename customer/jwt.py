import os
import jwt
import datetime

class JsonWebToken:
    secret_key = str(os.environ.get("SECRET_KEY"))

    def sign(self , payload_data):
        
        dt = datetime.datetime.now() + datetime.timedelta(hours = 1)   
        
        payload_data["exp"] = dt

        token = jwt.encode (

            
            payload = payload_data,

            key = self.secret_key,


        )
        
        return token.decode('utf-8')

   
    