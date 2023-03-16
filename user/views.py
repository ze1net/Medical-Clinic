# Rest Framework called generics, authentication, permissions  classes are used
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

# from models import user app models are called
from user.models import UserModel

# from serializers import user app serializers are called
from user.serializers import UserSerializer, UserProfileSerializer


# UserRegistrationView  for users registration
class UserRegistrationView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]


# UserProfileView for user profile
class UserProfileView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
