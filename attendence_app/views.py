from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from attendence_app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from attendence_app.models import *
from django.db import transaction
from .models import *

# @login_required(login_url='/')
# @login_required(login_url='login.html')

def loginStaff(request):
    # student: @student00 ,123happy@123
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        # check if user is valid
        user = authenticate(username=username, password=password)
        if user is not None:# if the user is logged in
            login(request,user)
            if request.user.is_staff:
                return redirect ('/')
            else:
                logout(request)
                return redirect ('/')
        else:# if the user is not logged in
            return render (request,"login.html")
    return render (request,'login.html')

def loginStudent(request):
    # student: happy ps:@123456789
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        # check if user is valid
        user = authenticate(username=username, password=password)
        if user is not None:# if the user is logged in
            login(request,user)
            if request.user.is_superuser:
                logout(request)
                return redirect ('/')
            else:
                return redirect ('/')
        else:# if the user is not logged in
            return render (request,"login.html")
    return render (request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect ('/loginStudent')

def home(request):
    if request.user.is_anonymous:
        return redirect("/loginStudent")
    else:
        if (request.user.is_superuser or request.user.is_staff):
            attendences = Attendence.objects.all().order_by('subjects__subject', 'roll__roll')
            context = {
                "attendences": attendences
            }
            return render (request,"staff_index.html",context)
        else:
            return render (request,"profile.html")
        
def base(request):
    return render(request, "base.html")

def profile(request):
    current_user = request.user
    # return HttpResponse(current_user.first_name)
    context = {
        'records':Students.objects.filter(user_name = current_user),
        'staff_records':current_user
    }
    return render (request,"profile.html",context)

def take_attendance(request):
    if request.method == "POST":
        # Get the selected checkbox values from request.POST
        student_values = request.POST.getlist("attend[]")
        
        # Get all student UIDs for attendance tracking
        all_student_uids = set(student.uid for student in Students.objects.all())
        
        # Process each selected value
        for student_value in student_values:
            student_uid, sub_name, is_present_str = student_value.split(',')
            
            # Convert is_present_str to a boolean
            is_present = is_present_str.lower() == 'true'
            
            # Get the student object using the UID
            student = Students.objects.get(uid=student_uid)
            subject_instance, created = Subjects.objects.get_or_create(uid=sub_name)
            # return HttpResponse(f"{subject_instance} subname {sub_name}")
            # Get or create attendance record
            attendance, created = Attendence.objects.get_or_create(roll=student, subjects=subject_instance)
            
            # Update present_days or total_days based on is_present value
            if is_present:
                attendance.present_days += 1
            else:
                attendance.total_days += 1
            
            # Save the updated attendance record
            attendance.save()
            
            # Remove student UID from the set of all UIDs
            all_student_uids.discard(student_uid)
        
        # For students who didn't submit a checkbox (considered absent)
        for student_uid in all_student_uids:
            student = Students.objects.get(uid=student_uid)
            subject_instance, created = Subjects.objects.get_or_create(uid=sub_name)
            attendance, created = Attendence.objects.get_or_create(roll=student, subjects=subject_instance)
            
            attendance.total_days += 1
            attendance.save()
        
        # Redirect to a success page or render a response as needed
        return redirect( "/")
    else:
        return render(request, "take_attendance.html")


def attendance(request):
    if (request.user.is_superuser or request.user.is_staff):
        if request.method=="POST":
            sub_name = request.POST.get("select_subject")
            batch = request.POST.get("select_batch")
            if sub_name == "choose" or batch == "choose":
                return HttpResponse("Please select both subject and batch.")
            else:
                main_context = {
                    "sub_name":sub_name,
                    "batch":batch,
                    "students":Students.objects.filter(batch=batch)
                }
                return render(request,"take_attendance.html",main_context )
        else:
            batches = Students.objects.values_list('batch', flat=True).distinct()
            main_context = {
                "subjects": Subjects.objects.all(),
                "batches": batches
            }
            return render(request,"select_attendance.html",main_context )
        user = request.POST.get('attend')
        print(user)
        return render(request,"select_attendance.html",main_context )
        
    else:
        current_user = request.user
        students=Students.objects.filter(user_name = current_user)
        # return HttpResponse(students)
        main_context = {
            "attendences": Attendence.objects.filter(roll__in=students)
        }
        return render(request,"my_attendance.html",main_context )
    




# def faclogin(request):
#     if request.method=="POST":
#         user=EmailBackEnd.authenticate(request,
#             username=request.POST.get('email'),
#             password=request.POST.get('password'),)
#         if user!=None:
#             login(request,user)
#             user_type = user.user_type
#             if user_type == '1':
#                 return redirect('staff_home')
#             elif user_type == '2':
#                 return HttpResponse('This is staff panel')
#             else:
#                 return redirect('login')
#         else:
#             return redirect('login')
        
# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return render(request,'index.html')
        




# def HOME(request):
#     return render(request,'staff/home2.html')