from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serialisers import CustomerUserSerializer
from django.contrib.auth import authenticate


# registered 

class RegisterView(APIView):
    def post(self,request):
        serializer =CustomerUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

# login 
class LoginView(APIView):
    def post(self,request):
        from rest_framework_simplejwt.tokens import RefreshToken
        user = authenticate(username= request.data['username'], password = request.data['password'])
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
            )
        return Response({"detail":"Invalid Creditial"}, status=status.HTTP_401_UNAUTHORIZED)
