from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages, auth
from django.http import HttpResponse,HttpResponseRedirect
from .models import Jobs, CompanyProfile
from .models import Students
# from .forms import StudentForm
from django.shortcuts import render, get_object_or_404, redirect
# from .models import  CustomUser
# from django.contrib.auth import get_user_model 
# from django.contrib.auth import get_user_model
# Create your views here.

# def sample(request):
#     return render(request, 'sample.html')
# def loginn(request):
#     return render(request, 'login.html')
# def reg(request):
#     return render(request, 'registration.html')
# User=get_user_model()
def index(request):
    return render(request, 'index.html')
def jobs(request):
    return render(request, 'jobs.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def cjob(request):
    return render(request, 'cjob.html')
def blog(request):
    return render(request, 'blog.html')
def postjob(request):
    return render(request, 'postjob.html')
# def admin_index(request):
#     return render(request, 'admin/index.html')
def admin_index2(request):
    return render(request, 'admin/index-2.html')
def admin_profile(request):
    return render(request, 'admin/profile.html')
def admin_editprofile(request):
    return render(request, 'admin/edit-profile.html')
# def admin_students(request):
#     return render(request, 'admin/students.html')
def admin_company(request):
    return render(request, 'admin/company.html')
# def admin_addstudent(request):
#     return render(request, 'admin/addstudent.html')
def admin_studentadd(request):
    return render(request,'admin/student_add.html')
def ad_cprofile(request):
    return render(request, 'admin/ad_cprofile.html')

# def addjob(request):
#     return render(request, 'addjob.html')
def loginn(request):
    if request.method == "POST":
        username=request.POST['email']
        # email = request.POST['email']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_index2')
            elif user.is_staff:
                return redirect('sindex')
            else:
                return redirect('cindex')
        else:
            messages.info(request, "Invalid Login")
            return redirect('loginn')
    else:
        return render(request, 'login.html') 

def reg(request):
    if request.method == "POST":
        companyname = request.POST['companyname']
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        headquarter = request.POST['headquarter']
        ceo = request.POST['ceo']
        phoneNumber = request.POST['phoneNumber']
        # role=User.COMPANY
        
        
        if password == confirmPassword:
            # if User.objects.filter(companyname=companyname).exists():
            #     return render(request, 'registration.html', {'companyname_exists': True})
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email already exists') 
                return redirect('reg')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                company = CompanyProfile(user=user, companyname=companyname, headquarter=headquarter, ceo=ceo, contact=phoneNumber) 
                user.save()
                company.save()
                messages.success(request, 'Registration successful! You can Login now..')
                return redirect('loginn')
        else:
            messages.error(request, 'Password confirmation does not match')
            return redirect('reg')
    else:
        return render(request, 'registration.html')
    
def loggout(request):
    print('Logged Out')
    auth.logout(request)
    return redirect('/')

def sample2(request):
    return render(request, 'sample2.html')
def cindex(request):
   if request.user.is_authenticated:
        companyprofile = request.user.companyprofile
        return render(request, 'cindex.html', {'companyprofile': companyprofile})
def aboutuser(request):
    return render(request, 'aboutuser.html')
def contactuser(request):
    return render(request, 'contactuser.html')
def cprofile(request, companyprofile_id):
    companyprofile=CompanyProfile.objects.get(id=companyprofile_id)
    
    if request.method == "POST":
         addressline1 = request.POST.get('addressline1')
        #  contact2 = request.POST.get('contact2')
         website = request.POST.get('website')
         city = request.POST.get('city')
         state = request.POST.get('state')
         district = request.POST.get('district')
         country = request.POST.get('country')
         pincode = request.POST.get('pincode')
         companydp=request.FILES['companydp'] if 'companydp' in request.FILES else None
 
         companyprofile.addressline1 = addressline1
         companyprofile.website= website
         companyprofile.city=city
         companyprofile.district=district
         companyprofile.state=state
         companyprofile.country=country
         companyprofile.pincode=pincode 
         companyprofile.companydp=companydp

        
         companyprofile.save()
         
         messages.success(request, 'Profile updated successfully.')
         return redirect('cindex')
    else:
         print("NO")
    context={
        'companyprofile': companyprofile
    }
    return render(request, 'cprofile.html', context)

# def postjob(request, companyprofile_id):
#     # Use get_object_or_404 to get the CompanyProfile instance or raise a 404 error if not found
#     companyprofile = get_object_or_404(CompanyProfile, id=companyprofile_id)

#     if request.method == "POST":
#         website = request.POST.get('website')
#         companyprofile.website = website
#         companyprofile.save()
#         return redirect('cindex')
#     else:
#         print("NO")
#     context={
#         'companyprofile': companyprofile
#     }
#     job = Jobs.objects.all()
#     return render(request, 'postjob.html', {'job': job, 'companyprofile': companyprofile}, context)

def sindex(request):
    return render(request, 'sindex.html')
def studentloginn(request):
    if request.method == "POST":
        username=request.POST['email']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Invalid Login")
            return redirect('studentloginn')
    else:
        return render(request, 'studentlogin.html') 

from django.core.files.images import get_image_dimensions
from django.http import HttpResponseBadRequest

def addjob(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        jname = request.POST.get('jname') 
        salary = request.POST.get('salary')
        email = request.POST.get('email')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        link = request.POST.get('link')
        criteria=request.FILES['criteria'] if 'criteria' in request.FILES else None

        if criteria and not criteria.name.endswith('.pdf'):
            messages.error(request, 'Please upload a PDF file for the criteria.')
            return redirect('postjob')


        obj = Jobs()
        obj.cname = cname
        obj.jname = jname
        obj.salary = salary
        obj.email = email
        obj.sdate = sdate
        obj.edate = edate
        obj.link = link
        obj.criteria=criteria
        
        obj.save()
        messages.success(request, 'Job added successfully!')

       # Redirect to the doctors page
        return redirect('postjob')  # Redirect to the doctors page URL name
    
    return render(request, 'addjob.html')
def postjob(request):
    job = Jobs.objects.all()
    return render(request, 'postjob.html', {'job': job})




# edit_job

from django.shortcuts import render, get_object_or_404, redirect
from .models import Jobs

def edit_job(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    criteriafile = request.FILES.get('criteria')
    if request.method == 'POST':
        job.cname = request.POST.get('cname')
        job.jname = request.POST.get('jname')
        job.salary = request.POST.get('salary')
        job.email = request.POST.get('email')
        job.sdate = request.POST.get('sdate')
        job.edate = request.POST.get('edate')
        job.link = request.POST.get('link')
        # job.criteria = request.POST.FILES['criteria'] if 'criteria' in request.FILES else None
        if criteriafile:
            job.criteria = criteriafile
        # job.criteria = request.POST.get('criteria')
        job.save()
        # Redirect to a success page or back to the job listing page
        return redirect('postjob')  # Change 'job_listing' to the appropriate URL name
        
    return render(request, 'editjob.html', {'job': job})

# deletejob
from django.shortcuts import render, redirect
from .models import Jobs

# def delete_job(request, job_id):
#     try:
#         job = Jobs.objects.get(id=job_id)
#         job.delete()
#         # Redirect to a different page (e.g., job list or any other appropriate page)
#         return redirect('postjob')  # Replace 'job_list' with the appropriate URL name
#     except Jobs.DoesNotExist:
#         # Handle the case where the job does not exist (you can show an error message or redirect to an error page)
#         return redirect('postjob')  # Redirect to the job list page or an error page as needed
from django.shortcuts import render, get_object_or_404, redirect
from .models import Jobs

def delete_job(request, job_id):
    # Get the job object by id
    job = get_object_or_404(Jobs, id=job_id)
    
    if request.method == 'POST':
        # Set the is_active field to False
        job.is_active = False
        job.save()  # Save the updated job object with is_active=False
        return redirect('postjob')  # Redirect to a suitable page after deletion

    return render(request, 'delete_job.html', {'job': job})

def CRegistration(request):
    return render(request, 'registration.html')


def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_index')  # Redirect to admin dashboard
        else:
            # Invalid credentials, handle error or show message
            pass
    
    return render(request, 'admin/admin_login.html')



#jobs_table_view 
from django.shortcuts import render
from .models import Jobs  # Import your Jobs model here


def jobslist(request):
    job_list= Jobs.objects.all()
    context = {'job_list': job_list}
    return render(request, 'admin/admin_jobtable.html', context)

# def job_list(request):
#     # Retrieve data from the Jobs model
#     joblist = Jobs.objects.all()
    
#     # Pass the data to the template
#     return render(request, 'job_list.html', {'joblist': joblist})

from django.shortcuts import render
from .models import CompanyProfile

def companyprofilelist(request):
    company_profiles = CompanyProfile.objects.all()
    return render(request, 'admin/companyprofilelist.html', {'company_profiles': company_profiles})


def addstudents(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        email = request.POST.get('email')
        # passw = request.POST.get('passw')
        # password=request.POST.get('password')
        course = request.POST.get('course')
        department = request.POST.get('department')
        semester = request.POST.get('semester')

        obj = Students()
        obj.sname = sname
        obj.email = email
        # obj.passw = passw
        # obj.password = password
        obj.course = course
        obj.department = department
        obj.semester = semester
        
        
        obj.save()
        messages.success(request, 'Student added successfully!')

       # Redirect to the doctors page
        return redirect('admin_poststudent')  # Redirect to the doctors page URL name
    
    return render(request, 'admin/student_add.html')











def profc(request):
    return render(request,'admin/profc.html')
def admin_poststudent(request):
    stus=Students.objects.all()
    return render(request,'admin/admin_poststudent.html',{'stus': stus})

def search_company(request):
    if 'companyname' in request.GET:
        companyname = request.GET['companyname']
        # Perform the company name search, for example:
        company_profiles = CompanyProfile.objects.filter(companyname__icontains=companyname)
    else:
        company_profiles = CompanyProfile.objects.all()  # Display all company profiles if no search query

    return render(request, 'admin/companyprofilelist.html', {'company_profiles': company_profiles})
def search_student(request):
    studentname = request.GET.get('studentname', '')
    
    # Filter students based on the search query
    students = Students.objects.filter(sname__icontains=studentname)
    
    return render(request, 'admin/admin_poststudent.html', {'stus': students})
def search_course(request):
    semail= request.GET.get('semail', '')
    
    # Filter students based on the search query
    students = Students.objects.filter(email__icontains=semail)
    
    return render(request, 'admin/admin_poststudent.html', {'stus': students})
# def adsearch_company(request):
#     if 'companyname' in request.GET:
#         companyname = request.GET['companyname']
#         # Perform the company name search, for example:
#         job_list = CompanyProfile.objects.filter(companyname__icontains=companyname)
#     else:
#         job_list = CompanyProfile.objects.all()  # Display all company profiles if no search query

#     return render(request, 'admin/admin_jobtable.html', {'job_list': job_list})
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from .models import CompanyProfile

from django.shortcuts import render
from .models import CompanyProfile

def adsearch_company(request):
    companysname = request.GET.get('companysname', '')

    print("Search query:", companysname)

    # Search for the company
    job_list = CompanyProfile.objects.filter(companyname__icontains=companysname)

    print("Company list:", job_list)

    return render(request, 'admin/admin_jobtable.html', {'job_list': job_list})






def search_job(request):
    jobsname = request.GET.get('jobsname', '')
    print("Search query:", jobsname)  # Print the search query to console

    job_list = Jobs.objects.filter(jname__icontains=jobsname)
    print("Job list:", job_list)  # Print the job list to console

    return render(request, 'admin/admin_jobtable.html', {'job_list': job_list})


def edit_student(request):
    return render(request, 'edit_student.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Students

def edit_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    
    if request.method == 'POST':
        # Update student data based on form input
        student.sname = request.POST.get('sname')
        student.email = request.POST.get('email')
        student.password = request.POST.get('password')
        student.course = request.POST.get('course')
        student.department = request.POST.get('department')
        student.semester = request.POST.get('semester')
        student.save()
        return redirect('admin_poststudent')
    return render(request, 'admin/edit_student.html', {'student': student})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Students

def delete_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)

    # Mark the student as inactive
    student.is_active = False
    student.save()

    # Redirect to admin_poststudent view
    return redirect('admin_poststudent')
def delete_company(request):
    return render(request, 'admin/ad_deletecompany.html')


def ad_deletecompany(request, comp_id):
    company_profile = get_object_or_404(CompanyProfile, id=comp_id)

    if request.method == 'POST':
        company_profile.is_active= False
        company_profile.save()
        return redirect('companyprofilelist')  # Redirect to a relevant URL after deletion

    return render(request, 'admin/ad_deletecompany.html', {'company_profile': company_profile})


import os
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.conf import settings
from django.views import View
from django.utils.text import slugify
from .models import Jobs

class download_criteria(View):
    def get(self, request, job_id):
        # Get the job and retrieve the criteria file path
        job = get_object_or_404(Jobs, pk=job_id)
        criteria_path = job.criteria.path

        if os.path.exists(criteria_path):
            with open(criteria_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{slugify(os.path.basename(criteria_path))}"'
                return response
        else:
            raise Http404("File not found")

# def addelete_job(request, jobb_id):
#     # Get the job object by id
#     jobb = get_object_or_404(Jobs, id=jobb_id)
    
#     if request.method == 'POST':
#         # Set the is_active field to False
#         jobb.is_active = False
#         jobb.save()  # Save the updated job object with is_active=False
#         return redirect('jobslist')  # Redirect to a suitable page after deletion

#     return render(request, 'delete_job.html', {'jobb': jobb})





from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from pathlib import Path
from django.conf import settings
from website.models import Students  # Replace `your_app` with the actual app name

def generate_pdf(request):
    # Your existing code for template path, context, and response
    template_path = 'admin/admin_poststudent.html'
    students = Students.objects.all()  # Retrieve students data

    context = {'students': students}

    # Construct the PDF file path
    pdf_file_path = str(Path(settings.MEDIA_ROOT) / 'temp_students_list.pdf')

    # Rest of your existing code for PDF generation
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf_file_path}"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html.escape(str(pisa_status.err)) + '</pre>')

    return response


from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Students  # Assuming your student model is named 'Students'

def stureg(request):
    if request.method == "POST":
        studentname = request.POST.get('studentname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        course = request.POST.get('course')
        phoneNumber = request.POST.get('phoneNumber')

        # Check if passwords match
        if password == confirmPassword:
            # Check if the email already exists
            if Students.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('stureg')
            else:
                # Create the student object
                student = Students(studentname=studentname, email=email, password=password, course=course, phoneNumber=phoneNumber)
                student.save()

                messages.success(request, 'Registration successful! You can log in now.')
                return redirect('loginn')
        else:
            messages.error(request, 'Password confirmation does not match')
            return redirect('stureg')
    else:
        return render(request, 'sregistration.html')

def sloginn(request):
    if request.method == "POST":
        username=request.POST['email']
        # email = request.POST['email']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_index2')
            elif user.is_staff:
                return redirect('sindex')
            else:
                return redirect('cindex')
        else:
            messages.info(request, "Invalid Login")
            return redirect('loginn')
    else:
        return render(request, 'login.html') 
