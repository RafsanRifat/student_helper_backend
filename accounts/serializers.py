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
    subject = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'institute_name', 'subject']
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
        subject = self.validated_data['subject']
        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user.set_password(password)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user, institute_name=institute_name, subject=subject)
        return user


# This Serializer give response of teacher custom fields after creating Teacher instance
class TeacherSignupSerializer2(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Teacher
        fields = ['username', 'email', 'institute_name', 'subject']
        extra_kwargs = {
            'password': {'write_only': True}
        }


# Student Signup Serializer
class StudentSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    institute_name = serializers.CharField(write_only=True)
    class_name = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'institute_name', 'class_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        institute_name = self.validated_data['institute_name']
        class_name = self.validated_data['class_name']

        if password != password2:
            raise serializers.ValidationError("Password doesn't match")
        user.set_password(password)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user, institute_name=institute_name, class_name=class_name)
        return user


# This Serializer give response of teacher custom fields after creating Teacher instance
class StudentSignupSerializer2(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Student
        fields = ['class_name', 'institute_name', 'username', 'email', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
