from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["_id", "email", "password", "name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    # override validate method not to accept additional fields
    # TODO: create a validation function so that can be used in other serializers
    def validate(self, data):

        if hasattr(self, "initial_data"):
            additional_keys = set(self.initial_data.keys()) - set(self.fields.keys())

            if additional_keys:
                raise ValidationError("Unknown fields: {}".format(additional_keys))

        return data


class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

    # override validate method not to accept additional fields
    # TODO: create a validation function so that can be used in other serializers
    def validate(self, data):

        if hasattr(self, "initial_data"):
            additional_keys = set(self.initial_data.keys()) - set(self.fields.keys())

            if additional_keys:
                raise ValidationError("Unknown fields: {}".format(additional_keys))

        return data
