from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import Task_Form, AddCourseForm
from .models import Task


# Create your views here.

def faculty_homepage(request):
    return render(request, 'facultyapp/FacultyHomePage.html')

# def view_student_list(request):
#     students = StudentList.objects.all()
#     return render(request, 'facultyapp/students.html')

def add_blog(request):
    if request.method == "POST":
        form = Task_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:add_blog')
    else:
        form = Task_Form()
    tasks = Task.objects.all()
    return render(request, 'facultyapp/BlogSiteManager.html', {'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('facultyapp:add_blog')

from .forms import AddCourseForm
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:faculty_homepage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/AddCourse.html', {'form': form})


from .models import AddCourse
from adminapp.models import StudentList

def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/students.html', context)
