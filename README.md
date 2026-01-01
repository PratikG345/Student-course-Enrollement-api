
### Student–Course Enrollment REST API
A Student–Course Enrollment REST API built using Django REST Framework to model and manage enrollments with a focus on data integrity, state management, and disciplined API design.
This project emphasizes backend decision-making over feature breadth.

## Techstack: 
Python,Django,DjangoRestFramework, sqlite3

## Getting Started:
__Step 1:__ Clone the repository: 
```
git clone https://github.com/PratikG345/Student-course-Enrollment-api.git
```

__Step 2:__ Create virtual environment by using 
```
py -m venv env
```

__Step 3:__ Activate the virtual environment by 
```
env/Scripts/activate
```
__Step 4:__ navigate to project 
```
cd course
```
__Step 5:__ run on local server 
```
python3 manage.py runserver
```
## API Endpoints: 
1. __GET students/__ - list all students
2. __GET students/{id}/__ - Retrive details of single student
3. __POST students/add/__ - create a student
4. __GET students/{id}/enrollments/__ - to see courses taken by single student
5. __GET courses/__ - list all courses
6. __GET courses/{id}/__ - Retrive details of single course
7. __POST courses/add/__ - create a course
8. __GET courses/{id}/enrollments/__ - enrollments of single course
9. __GET enrollments/__ - list all enrollments
10. __GET enrollments/{id}/__ - Retrive details of single enrollments
11. __POST enrollments/add/__ - create a enrollment
12. __POST enrollments/{id}/status/__ - CHange status of a enrollment from ACTIVE TO DROPPED or vice versa

## Project Scope
This project was intentionally kept simple to strengthen backend fundamentals:
* Represent student–course relationships using a dedicated Enrollment model
* Enforce business constraints to prevent invalid states such as duplicate enrollments
* Design context-driven endpoints to access enrollments from both course and student perspectives
* Handle state transitions (e.g., ACTIVE, DROPPED) without deleting records
* Apply serializer separation to clearly distinguish between create, read, and update operatio

No authentication or advanced features were added by design.

## Key Learnings
* Learned to model many-to-many relationships explicitly using an intermediate entity instead of relying on implicit abstractions.
* Understood the importance of relationship-level constraints and enforced data integrity by preventing duplicate enrollments.
* Practiced designing context-aware APIs, where URL structure determines scope and response shape.
* Implemented state transitions (ACTIVE → DROPPED) to manage lifecycle changes without deleting data.
* Gained clarity on serializer intent, using separate serializers for creation, reading, and partial updates to avoid accidental writes.
* Learned to correctly handle partial updates by distinguishing between create and update operations in Django REST Framework.
