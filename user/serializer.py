from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserConfirm

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        models = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            is_active=False
        )

        code = UserConfirm.generate_code()
        UserConfirm.objects.create(user=user, code=code)

        print(f"Код подтверждения для {user.username}: {code}")
        
        return user 
    
class UserConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)
    

