from django.urls import path
from .views import all_students,student_detail,create_student
from .views import all_courses,course_detail,create_course
from .views import all_enrollments,enrollment_detail,create_enrollment,enrollements_by_course,enrollments_by_name,change_status
urlpatterns = [
    # ------- Students Urls ----------------
    path('students/',all_students,name="all_students"),
    path('students/<int:pk>',student_detail,name="student_detail"),
    path('students/add',create_student,name="create_student"),
    path('students/<int:pk>/enrollments/',enrollments_by_name,name="enrollments_by_name"),
    
    # ------- Course Urls -------------------
    path('courses/',all_courses,name="all_courses"),
    path('courses/<int:pk>',course_detail,name="course_detail"),
    path('courses/add',create_course,name="create_course"),
    path('courses/<int:pk>/enrollments/',enrollements_by_course,name="enrollements_by_course"),
    
    # ---------- Enrollment Urls -------------
    path('enrollments/',all_enrollments,name="all_enrollments"),
    path('enrollments/<int:pk>',enrollment_detail,name="enrollment_detail"),
    path('enrollments/add',create_enrollment,name="create_enrollment"),
    path('enrollments/<int:pk>/status',change_status,name="change_status")
]
