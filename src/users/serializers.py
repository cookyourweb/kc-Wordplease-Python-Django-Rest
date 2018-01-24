from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'last_login']
        extra_kwargs = {
                            'first_name': {'required': True},
                            'last_name': {'required': True},
                            'email': {'required': True},
                            'password': {'required': True}
                        }

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

