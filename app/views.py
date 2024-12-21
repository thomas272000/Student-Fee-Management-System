from django.shortcuts import render,redirect
from .models import Student,FeeCategory,StudentFees,AdminModel
from django.db.models import Sum
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages


# Create your views here.



def register_admin(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        dob = data.get('dob')


        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register_admin')

        admin = AdminModel()
        admin.name = name
        admin.username = username
        admin.email = email
        admin.password = make_password(password)
        admin.dob = dob
        admin.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('/')

    return render(request, 'register_admin.html')


def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        try:
            admin = AdminModel.objects.get(username=username)
            if check_password(password, admin.password):

                request.session['admin_id'] = admin.id
                request.session['admin_username'] = admin.username
                messages.success(request, "Login successful!")
                return redirect('/dashboard')
            else:
                messages.error(request, "Invalid password!")
        except AdminModel.DoesNotExist:
            messages.error(request, "Invalid username!")

    return render(request, 'login_admin.html')
def logout_admin(request):
    if 'admin_id' in request.session:
        del request.session['admin_id']
        del request.session['admin_username']
    messages.success(request, "Logged out successfully!")
    return redirect('/')


def student_list(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def delete_student(request, id):
    if 'admin_id' not in request.session:
        return redirect('/')
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/students/')


def add_student(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        class_name = data.get('class_name')
        roll_number = data.get('roll_number')
        email = data.get('email')
        student = Student()
        student.first_name = first_name
        student.last_name = last_name
        student.class_name = class_name
        student.roll_number = roll_number
        student.email = email
        student.save()
        return redirect('/students/')
    return render(request, 'add_student.html')


def update_student(request, id):
    if 'admin_id' not in request.session:
        return redirect('/')
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        student.first_name = data.get('first_name')
        student.last_name = data.get('last_name')
        student.class_name = data.get('class_name')
        student.roll_number = data.get('roll_number')
        student.email = data.get('email')
        student.save()
        return redirect('/students/')
    return render(request, 'update_student.html', {'student': student})



def fee_category_list(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    fee_categories = FeeCategory.objects.all()
    return render(request, 'fee_category_list.html', {'fee_categories': fee_categories})


def add_fee_category(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        fee_type = data.get('fee_type')
        amount = data.get('amount')
        fee_category = FeeCategory()
        fee_category.name = name
        fee_category.fee_type = fee_type
        fee_category.amount = amount
        fee_category.save()
        return redirect('/fee-categories/')
    return render(request, 'add_fee_category.html')


def update_fee_category(request, id):
    if 'admin_id' not in request.session:
        return redirect('/')
    fee_category = FeeCategory.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        fee_category.name = data.get('name')
        fee_category.fee_type = data.get('fee_type')
        fee_category.amount = data.get('amount')
        fee_category.save()
        return redirect('/fee-categories/')
    return render(request, 'update_fee_category.html', {'fee_category': fee_category})


def delete_fee_category(request, id):
    if 'admin_id' not in request.session:
        return redirect('/')
    fee_category = FeeCategory.objects.get(id=id)
    fee_category.delete()
    return redirect('/fee-categories/')



def assign_fees(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        data = request.POST
        student_id = data.get('student_id')
        fee_category_id = data.get('fee_category_id')
        due_date = data.get('due_date')
        status = data.get('status')
        student_fee = StudentFees()
        student_fee.student_id = student_id
        student_fee.fee_category_id = fee_category_id
        student_fee.due_date = due_date
        student_fee.status = status
        student_fee.save()
        return redirect('/students/')
    students = Student.objects.all()
    fee_categories = FeeCategory.objects.all()
    return render(request, 'assign_fees.html', {'students': students, 'fee_categories': fee_categories})


def payment_status(request, id):
    if 'admin_id' not in request.session:
        return redirect('/')
    student = Student.objects.get(id=id)
    student_fees = StudentFees.objects.filter(student_id=id)
    return render(request, 'payment_status.html', {'student': student, 'student_fees': student_fees})


def update_payment_status(request, id):
    if 'admin_id' not in request.session:
        return redirect('/')
    student_fee = StudentFees.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        student_fee.status = data.get('status')
        student_fee.paid_date = data.get('paid_date')
        student_fee.amount_paid = data.get('amount_paid')
        student_fee.save()
        return redirect("/dashboard")
    return render(request, 'update_payment_status.html', {'student_fee': student_fee})




def dashboard(request):
    if 'admin_id' not in request.session:
        return redirect('/login/')

    students_with_due_fees = StudentFees.objects.filter(status='Due')
    due_fees_with_outstanding = [
        {
            'student': fee.student,
            'fee_category': fee.fee_category,
            'amount_due': fee.fee_category.amount - fee.amount_paid,
            'due_date': fee.due_date,
            'fee_id': fee.id,
        }
        for fee in students_with_due_fees
    ]
    total_fees_collected = StudentFees.objects.filter(status='Paid').aggregate(
        total_collected=Sum('amount_paid')
    )['total_collected'] or 0


    outstanding_fees = sum(fee['amount_due'] for fee in due_fees_with_outstanding)


    recent_payments = StudentFees.objects.filter(status='Paid').order_by('-paid_date')[:10]

    return render(request, 'dashboard.html', {
        'total_fees_collected': total_fees_collected,
        'outstanding_fees': outstanding_fees,
        'recent_payments': recent_payments,
        'students_with_due_fees': due_fees_with_outstanding,
        'admin_username': request.session.get('admin_username'),
    })
