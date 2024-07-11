from django.utils.timezone import localtime
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('uuid', 'username', 'email', 'phone', 'created_at', 'is_approved', 'is_admin')
        extra_kwargs = {'password': {'write_only': True}}

    def get_created_at(self, obj):
        local_time = localtime(obj.created_at)
        return local_time.strftime('%d/%m/%Y %I:%M %p')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password']
        )
        return user

class CustomUserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password1']
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user_id'] = str(user.uuid)
        token['username'] = user.username
        # Add more custom fields if needed

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = CustomUserSerializer(self.user)
        data.update(serializer.data)
        return data
