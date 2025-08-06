from django.shortcuts import render, get_object_or_404
from .forms import StudentUserForm, StudentDetailsForm, StaffUserForm, StaffDetailsForm, LiberianUserForm, LiberianDetailsForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Book, Borrowed, Student, Staff

# Create your views here.
def index(request):
    return render(request, 'index.html')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm

def is_liberian(user):
    return hasattr(user, 'liberian') or user.is_superuser

def liberianpanel(request):
    return render(request, 'liberianpanel.html')

def staffpanel(request):
    return render(request, 'staffpanel.html')

def studentpanel(request):
    return render(request, 'studentpanel.html')

@user_passes_test(is_liberian)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LMS-booklist')
        else:
            print ("Form errors:", form.errors)
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})



from django.contrib.auth import authenticate, login

def liberianlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        form1 = LiberianUserForm()
        form2 = LiberianDetailsForm()
        if user is not None and hasattr(user, 'liberian'):
            login(request, user)
            return redirect('LMS-liberiandashboard')
        else:
            error_message = "Incorrect username or password."
            return render(request, 'liberianlogin.html', {'form1': form1, 'form2': form2, 'error_message': error_message})
    else:
        form1 = LiberianUserForm()
        form2 = LiberianDetailsForm()
    return render(request, 'liberianlogin.html', {'form1': form1, 'form2': form2})

from django.contrib.auth import authenticate, login

def stafflogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        form1 = StaffUserForm()
        form2 = StaffDetailsForm()
        if user is not None and hasattr(user, 'staff'):
            login(request, user)
            return redirect('LMS-staffdashboard')
        else:
            error_message = "Incorrect username or password."
            return render(request, 'stafflogin.html', {'form1': form1, 'form2': form2, 'error_message': error_message})
    else:
        form1 = StaffUserForm()
        form2 = StaffDetailsForm()
    return render(request, 'stafflogin.html', {'form1': form1, 'form2': form2})

from django.contrib.auth import authenticate, login

def studentlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'student'):
            login(request, user)
            return redirect('LMS-studentdashboard')
        else:
            form1 = StudentUserForm()
            form2 = StudentDetailsForm()
            error_message = "Incorrect username or password."
            return render(request, 'studentlogin.html', {'form1': form1, 'form2': form2, 'error_message': error_message})
    else:
        form1 = StudentUserForm()
        form2 = StudentDetailsForm()
    return render(request, 'studentlogin.html', {'form1': form1, 'form2': form2})

def studentsignup(request):
    if request.method == 'POST':
        form1 = StudentUserForm(request.POST)
        form2 = StudentDetailsForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.first_name = form2.cleaned_data.get('FirstName', '')
            user.last_name = form2.cleaned_data.get('LastName', '')
            user.email = form1.cleaned_data['email']
            user.save()
            details = form2.save(commit=False)
            details.user = user
            details.FirstName = form2.cleaned_data.get('FirstName', '')
            details.LastName = form2.cleaned_data.get('LastName', '')
            details.save()
            return redirect('LMS-studentlogin')
    else:
        form1 = StudentUserForm()
        form2 = StudentDetailsForm()
    return render(request, 'studentsignup.html', {'form1': form1, 'form2': form2})

def staffsignup(request):
    if request.method == 'POST':
        form1 = StaffUserForm(request.POST)
        form2 = StaffDetailsForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.first_name = form2.cleaned_data.get('FirstName', '')
            user.last_name = form2.cleaned_data.get('LastName', '')
            user.email = form1.cleaned_data['email']
            user.save()
            details = form2.save(commit=False)
            details.user = user
            details.FirstName = form2.cleaned_data.get('FirstName', '')
            details.LastName = form2.cleaned_data.get('LastName', '')
            details.save()
            return redirect('LMS-stafflogin')
    else:
        form1 = StaffUserForm()
        form2 = StaffDetailsForm()
    return render(request, 'staffsignup.html', {'form1': form1, 'form2': form2})

def liberiansignup(request):
    if request.method == 'POST':
        form1 = LiberianUserForm(request.POST)
        form2 = LiberianDetailsForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.first_name = form2.cleaned_data.get('FirstName', '')
            user.last_name = form2.cleaned_data.get('LastName', '')
            user.email = form1.cleaned_data['email']
            user.save()
            details = form2.save(commit=False)
            details.user = user
            details.FirstName = form2.cleaned_data.get('FirstName', '')
            details.LastName = form2.cleaned_data.get('LastName', '')
            details.save()
            return redirect('LMS-liberianlogin')
    else:
        form1 = LiberianUserForm()
        form2 = LiberianDetailsForm()
    return render(request, 'liberiansignup.html', {'form1': form1, 'form2': form2})

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def studentdashboard(request):
    return render(request, 'studentdashboard.html')

@login_required
def staffdashboard(request):
    return render(request, 'staffdashboard.html')

@login_required
def student_profile(request):
    user = request.user
    student = None
    try:
        student = user.student
    except Student.DoesNotExist:
        student = None
    return render(request, 'studentprofile.html', {'student': student, 'user': user})

@login_required
def liberiandashboard(request):
    return render(request, 'liberiandashboard.html')

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def user_logout(request):
    logout(request)
    # Redirect based on user type
    if hasattr(request.user, 'liberian'):
        return redirect('LMS-liberianlogin')
    elif hasattr(request.user, 'student'):
        return redirect('LMS-studentlogin')
    elif hasattr(request.user, 'staff'):
        return redirect('LMS-stafflogin')
    else:
        return redirect('LMS-index')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = request.user
    borrowed = None
    if request.method == 'POST':
        # Check if user is student or staff
        if hasattr(user, 'student'):
            borrowed = Borrowed.objects.create(BookID=book, student=user.student)
        elif hasattr(user, 'staff'):
            borrowed = Borrowed.objects.create(BookID=book, staff=user.staff)
        return redirect('LMS-borrowedbooks')
    return render(request, 'borrow_book.html', {'book': book})

@login_required
def return_book(request, borrow_id):
    borrowed = get_object_or_404(Borrowed, pk=borrow_id)
    if request.method == 'POST':
        borrowed.delete()
        return redirect('LMS-borrowedbooks')
    return render(request, 'return_book.html', {'borrowed': borrowed})

@login_required
def borrowed_books(request):
    user = request.user
    borrowed_books = []
    if hasattr(user, 'student'):
        borrowed_books = Borrowed.objects.filter(student=user.student)
    elif hasattr(user, 'staff'):
        borrowed_books = Borrowed.objects.filter(staff=user.staff)
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})

@login_required
def issued_books(request):
    borrowed_books = Borrowed.objects.all()
    return render(request, 'issued_books.html', {'borrowed_books': borrowed_books})

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from .forms import LiberianStudentStatusForm, LiberianStaffStatusForm
from .models import Student, Staff
from django.shortcuts import render

def is_liberian(user):
    return hasattr(user, 'liberian') or user.is_superuser

@user_passes_test(is_liberian)
def registered_students_list(request):
    students = Student.objects.all().values('id', 'FirstName', 'MatriculationNumber', 'Status')
    return render(request, 'registered_students_list.html', {'students': students})

@user_passes_test(is_liberian)
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'student_detail.html', {'student': student})

@user_passes_test(is_liberian)
def edit_student_status(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = LiberianStudentStatusForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('LMS-student-detail', student_id=student.id)
    else:
        form = LiberianStudentStatusForm(instance=student)
    return render(request, 'edit_student_status.html', {'form': form, 'student': student})

@user_passes_test(is_liberian)
def edit_staff_status(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    if request.method == 'POST':
        form = LiberianStaffStatusForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('LMS-manage-staff-status')
    else:
        form = LiberianStaffStatusForm(instance=staff)
    return render(request, 'edit_staff_status.html', {'form': form, 'staff': staff})
