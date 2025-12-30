from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student,Course,Enrollment
from .serializer import StudentSerializer,CourseSerializer,EnrollmentReadSerializer,EnrollmentCreateSerializer,EnrollmentDropSerializer
# ---- Importing filter serializers here
from .serializer import StudentEnrollSerializer,CourseEnrollSerializer

# Create your views here.

# ------------------------ Student related Views --------------------------
@api_view(['GET'])
def all_students(req):
    student = Student.objects.all()
    stud = StudentSerializer(student,many=True)
    return Response(stud.data)

@api_view(['GET'])
def student_detail(req,pk):
    student = get_object_or_404(Student,pk=pk)
    if req.method == 'GET':
        stud = StudentSerializer(student)
        return Response(stud.data)

@api_view(['POST'])
def create_student(req):
    stud = StudentSerializer(data=req.data)
    if stud.is_valid():
        stud.save()
        return Response(stud.data,status=status.HTTP_201_CREATED)
    return Response(stud.errors,status=status.HTTP_400_BAD_REQUEST)



# ------------------------Course Related Views -------------------------------

@api_view(['GET'])
def all_courses(req):
    course = Course.objects.all()
    course1 = CourseSerializer(course,many=True)
    return Response(course1.data)

@api_view(['GET'])
def course_detail(req,pk):
    course = get_object_or_404(Course,pk=pk)
    if req.method == 'GET':
        course1 = CourseSerializer(course)
        return Response(course1.data)

@api_view(['POST'])
def create_course(req):
    course1 = CourseSerializer(data=req.data)
    if course1.is_valid():
        course1.save()
        return Response(course1.data,status=status.HTTP_201_CREATED)
    return Response(course1.errors,status=status.HTTP_400_BAD_REQUEST)


# --------------------- Enrollment Related Views ---------------------------

@api_view(['GET'])
def all_enrollments(req):
    enroll = Enrollment.objects.all()
    enrolls = EnrollmentReadSerializer(enroll,many=True)
    return Response(enrolls.data)

@api_view(['GET'])
def enrollment_detail(req,pk):
    enroll = get_object_or_404(Enrollment,pk=pk)
    if req.method == 'GET':
        enrolls = EnrollmentReadSerializer(enroll)
        return Response(enrolls.data)

@api_view(['POST'])
def create_enrollment(req):
    enrolls = EnrollmentCreateSerializer(data=req.data)
    if enrolls.is_valid():
        enrolls.save()
        return Response(enrolls.data,status=status.HTTP_201_CREATED)
    return Response(enrolls.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def change_status(req,pk):
    enroll = get_object_or_404(Enrollment,pk=pk)
    
    if req.method == 'GET':
        enrolls = EnrollmentReadSerializer(enroll)
        return Response(enrolls.data)
    
    if req.method == 'PUT':
        enrolls = EnrollmentDropSerializer(enroll,data=req.data)
        if enrolls.is_valid():
            enrolls.save()
            return Response(enrolls.data,status=status.HTTP_201_CREATED)
        return Response(enrolls.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def enrollements_by_course(req,pk):
    enroll = Enrollment.objects.filter(course_id=pk)
    enrolls = CourseEnrollSerializer(enroll,many=True)
    return Response(enrolls.data)

@api_view(['GET'])
def enrollments_by_name(req,pk):
    enroll = Enrollment.objects.filter(student_id=pk)
    enrolls = StudentEnrollSerializer(enroll,many=True)
    return Response(enrolls.data)