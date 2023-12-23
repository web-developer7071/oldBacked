from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import User
# from django.db.models.fields import EmailField
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    # email = EmailField(max_length=None, min_length=None, allow_blank=False)
    password = serializers.CharField(required = True, style = {'input_type': 'password'})
    # password = serializers.CharField(write_only = True, required = True, help_text = 'Leave empty if no change needed', style = {'input_type': 'password', 'placeholder': 'Password'})
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'user_type', 'admin_user', 'admin_service_type','Today_Status', 'Current_Status', 'Collected_No', 'Running_No']

        # if this is set then password not return
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
    #            Or
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.Model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance


class LoadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'is_superuser', 'user_type', 'admin_user', 'admin_service_type','Today_Status', 'Current_Status', 'Collected_No', 'Running_No']