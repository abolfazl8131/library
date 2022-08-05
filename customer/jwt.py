import os
import jwt


class JsonWebToken:
    secret_key = str(os.environ.get("SECRET_KEY"))

    def sign(self , payload_data):
        payload_data["exp"] = 600

        token = jwt.encode (

            
            payload = payload_data,

            key = self.secret_key,

        )
        
        return token.decode('utf-8')

    def validate(self, token):
        pass

    