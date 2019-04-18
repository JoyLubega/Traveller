from rest_framework.response import Response
from rest_framework.views import status


def validate_user_registration(fn):
    def decorated(*args, **kwargs):
        
        username = args[0].request.data.get("username", "")
        email = args[0].request.data.get("email", "")
        password = args[0].request.data.get("password", "")
        if not username:
            return Response(
                data={
                    "message": "Username is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not email:
            return Response(
                data={
                    "message": "Email is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not password:
            return Response(
                data={
                    "message": "Password is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated

def validate_user_login(fn):
    def decorated(*args, **kwargs):
    
        username = args[0].request.data.get("username", "")
        password = args[0].request.data.get("password", "")
        if not username:
            return Response(
                data={
                    "message": "Username is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not password:
            return Response(
                data={
                    "message": "Password is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated

def validate_flight_data(fn):
    def decorated(*args, **kwargs):
    
        destination = args[0].request.data.get("destination", "")
        pickup = args[0].request.data.get("pickup", "")
        departure_date = args[0].request.data.get("departure_date", "")
        return_date = args[0].request.data.get("return_date", "")
        no_travellers=args[0].request.data.get("no_travellers", "")
        passport_number = args[0].request.data.get("passport_number", "")
        
        if not destination and not pickup and not departure_date and not return_date and not no_travellers and not passport_number:
            return Response(
                data={
                    "message": "All Data is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return fn(*args, **kwargs)
    return decorated