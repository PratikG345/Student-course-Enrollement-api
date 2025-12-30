from rest_framework import serializers
from .models import Student,Course,Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        
        
class EnrollmentReadSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    class Meta:
        model = Enrollment
        fields = "__all__"
        
class EnrollmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['student','course']
        
    def validate(self, data):
        student = data['student']
        course = data['course']
        
        if Enrollment.objects.filter(
            student=student,
            course = course
        ).exists():
            raise serializers.ValidationError("Student Already Enrolled in this Course")
        
        return data
        
class CourseEnrollSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    class Meta:
        model = Enrollment
        fields = ['student','enrolled_at','status']
        
class StudentEnrollSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    class Meta:
        model = Enrollment
        fields = ['course','enrolled_at','status']

class EnrollmentDropSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Enrollment
        fields = ['status']