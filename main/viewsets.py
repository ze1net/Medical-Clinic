from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import AboutUsModel
from .permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import AboutUsModelSerializer, ContactUsModelSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    serializer_class = AboutUsModelSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return AboutUsModel.objects.filter(is_information_added=True)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj:
            return obj
        else:
            return AboutUsModel.objects.create()

    def perform_update(self, serializer):
        serializer.save()


class ContactUsViewSet(viewsets.ViewSet):
    serializer_class = ContactUsModelSerializer

    def create(self, request):
        serializer = ContactUsModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Process the contact form data and send an email
        # You can replace this with your own implementation
        return Response({'message': 'Thank you for contacting us!'})

    def list(self, request):
        return Response({'message': 'This endpoint accepts POST requests only.'})
