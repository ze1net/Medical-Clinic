from rest_framework import serializers
from .models import ContactUsModel, AboutUsModel


class ContactUsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = '__all__'


class AboutUsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsModel
        fields = '__all__'

    def validate(self, data):
        if self.instance and self.instance.is_information_added:
            # If the information has already been added, don't allow editing
            raise serializers.ValidationError("Cannot edit the About Us information")
        return data