from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm  # Import the form you created

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_students')  # Redirect to the list page
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def show_students(request):
    students = Student.objects.all()
    return render(request, 'students/show_students.html', {'students': students})

def search_student(request):
    students = []
    query = None

    if request.method == "POST":
        query = request.POST.get('query', '').strip()

        if query.isdigit():  # Search by ID if query is numeric
            students = Student.objects.filter(id=query)
        else:  # Search by first_name otherwise
            students = Student.objects.filter(first_name__icontains=query)

    return render(request, 'students/search_student.html', {'students': students, 'query': query})


def update_student(request):
    context = {}

    # Handle GET request to fetch student data
    if 'id' in request.GET:
        student_id = request.GET['id']
        try:
            student = Student.objects.get(id=student_id)
            context['student'] = student
        except Student.DoesNotExist:
            context['error'] = "Student with this ID does not exist."

    # Handle POST request to update student data
    if request.method == 'POST':
        student_id = request.POST.get('id')
        student = get_object_or_404(Student, id=student_id)
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.save()
        context['success'] = "Student information updated successfully!"
        context['student'] = student  # Send the updated student data back

    return render(request, 'students/update_student.html', context)

def delete_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')  # Get the student ID from form input
        try:
            # Attempt to fetch and delete the student
            student = Student.objects.get(id=student_id)
            student.delete()
            return render(request, 'students/delete_student.html', {
                'success': f"Student with ID {student_id} has been deleted successfully!"
            })
        except Student.DoesNotExist:
            # Handle the case where the student doesn't exist
            return render(request, 'students/delete_student.html', {
                'error': f"Student with ID {student_id} does not exist."
            })
    return render(request, 'students/delete_student.html')
