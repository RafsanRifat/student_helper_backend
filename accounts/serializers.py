from rest_framework import serializers
from .models import User, Teacher, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_teacher', 'is_student']


# Teacher Signup serializer
class TeacherSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    institute_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'institute_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        institute_name = self.validated_data['institute_name']
        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user, institute_name=institute_name)
        return user


# This Serializer give response of teacher custom fields after creating Teacher instance
class TeacherSignupSerializer2(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='User.username')
    email = serializers.ReadOnlyField(source='User.email')

    class Meta:
        model = Teacher
        fields = ['username', 'email', 'institute_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }


# Student Signup Serializer
class StudentSignupSerializer(serializers.ModelSerializer):
    institute_name = serializers.CharField(write_only=True)
    class_name = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'institute_name', 'class_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }
