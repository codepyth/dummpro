from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .signals import send_edit_email
# Create your views here.
class LoginView(TemplateView):
    template_name = 'loginsignup.html'



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                info = Registration.objects.get(user=user)
                if info:
                    return redirect('/status/')
            except Registration.DoesNotExist:
                return redirect('/start/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('/')
    return render(request, 'loginsignup.html')

@login_required
def check_view(request):
    return render(request, 'forms.html')

@login_required
def status(request):
    user = request.user
    try:
        data = Registration.objects.get(user=user)
        context = {
            'data': data
        }
        return render(request, 'status.html', context=context)
    except:
        pass
    return redirect('start')

def update_data(request):
    user = request.user
    data = Registration.objects.get(user=user)
    if request.method == 'POST':
        # Access form fields from request.POST

        email = request.POST.get('email')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        relationship = request.POST.get('relationship')
        occupation = request.POST.get('occupation')
        school_name = request.POST.get('school_name')
        grade = request.POST.get('grade')
        job_name = request.POST.get('job_name')
        job_company = request.POST.get('job_company')
        job_details = request.POST.get('job_details')
        company_name = request.POST.get('company_name')
        business_type = request.POST.get('business_type')
        company_details = request.POST.get('company_details')
        buisness_details = request.POST.get('buisness_details')
        passport_number = request.POST.get('passport_number')
        passport_expiry = request.POST.get('passport_expiry')
        nationality = request.POST.get('nationality')
        proof_of_origin = request.POST.get('proof_of_origin')
        origin_id_number = request.POST.get('origin_id_number')
        visa_status = request.POST.get('visa_status')
        visa_expiry_date = request.POST.get('visa_expiry_date')
        visa_document = request.POST.get('visa_document')
        profile_pic = request.POST.get('profile_pic')
        staying_in_rwanda_since = request.POST.get('staying_in_rwanda_since')
        living_with_dependents = 'living_with_dependents' in request.POST
        if living_with_dependents == "True":
            print(True)
        else :
            print(living_with_dependents)
        mobile_number = request.POST.get('mobile_number')
        whatsapp_number = request.POST.get('whatsapp_number')
        address_in_rwanda = request.POST.get('address_in_rwanda')
        province = request.POST.get('province')
        district = request.POST.get('district')
        sector = request.POST.get('sector')
        cell = request.POST.get('cell')
        country = request.POST.get('country')
        address = request.POST.get('address')
        contact_name = request.POST.get('contact_name')
        relation = request.POST.get('relation')
        contact_mobile = request.POST.get('contact_mobile')
        attachment1 = request.POST.get('attachment1')
        attachment2 = request.POST.get('attachment2')
        attachment3 = request.POST.get('attachment3')
        attachment4 = request.POST.get('attachment4')
        data.email=email
        data.name=name
        data.gender=gender
        data.dob=dob
        data.relationship=relationship
        data.occupation=occupation
        data.school_name=school_name
        data.grade=grade
        data.job_name=job_name
        data.job_company=job_company
        data.job_details=job_details
        data.company_name=company_name
        data.business_type=business_type
        data.company_details=company_details
        data.buisness_details=buisness_details
        data.passport_number=passport_number
        data.passport_expiry=passport_expiry
        data.nationality=nationality
        data.proof_of_origin=proof_of_origin
        data.origin_id_number=origin_id_number
        data.visa_status=visa_status
        data.visa_document=visa_document
        data.passport_picture=profile_pic
        data.visa_expiry_date=visa_expiry_date
        data.staying_in_rwanda_since=staying_in_rwanda_since
        data.living_with_dependents=living_with_dependents
        data.mobile_number=mobile_number
        data.whatsapp_number=whatsapp_number
        data.address_in_rwanda=address_in_rwanda
        data.province=province
        data.district=district
        data.sector=sector
        data.cell=cell
        data.emergency_country = country
        data.other_full_address = address
        data.contact_name = contact_name
        data.relation = relation
        data.emergency_mobile_number = contact_mobile
        data.attachment1 = attachment1
        data.attachment2 = attachment2
        data.attachment3 = attachment3
        data.attachment4 = attachment4
        data.applied_for_edit = True
        data.status = "PENDING"
        data.save()
        send_edit_email(user_name=request.user.username, user_email=request.user.email)
        # Create a new Registration instance with the provided data

        return redirect('status')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
            else:
                user = User.objects.create_user(username=username,email=username, password=password)
                user.save()
                messages.success(request, 'Account created. You can now log in.')
                return redirect('/')  # Redirect to the login page after successful signup
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'loginsignup.html')


from django.shortcuts import render, redirect,HttpResponse
from .models import Registration  # Import your model here
from datetime import datetime

def save_registration(request):
    user = request.user
    try:
        data = Registration.objects.get(user=user)
    except:
        data = Registration()
    if request.method == 'POST':
        # Access form fields from request.POST

        email = request.POST.get('email')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        relationship = request.POST.get('relationship')
        occupation = request.POST.get('occupation')
        school_name = request.POST.get('school_name')
        grade = request.POST.get('grade')
        job_name = request.POST.get('job_name')
        job_company = request.POST.get('job_company')
        job_details = request.POST.get('job_details')
        company_name = request.POST.get('company_name')
        business_type = request.POST.get('business_type')
        company_details = request.POST.get('company_details')
        buisness_details = request.POST.get('buisness_details')
        passport_number = request.POST.get('passport_number')
        passport_expiry = request.POST.get('passport_expiry')
        nationality = request.POST.get('nationality')
        proof_of_origin = request.POST.get('proof_of_origin')
        origin_id_number = request.POST.get('origin_id_number')
        visa_status = request.POST.get('visa_status')
        visa_expiry_date = request.POST.get('visa_expiry_date')
        visa_document = request.POST.get('visa_document')
        profile_pic = request.POST.get('profile_pic')
        staying_in_rwanda_since = request.POST.get('staying_in_rwanda_since')
        living_with_dependents = 'living_with_dependents' in request.POST
        if living_with_dependents == "True":
            request.session['living_with_dependents'] = True
        else :
            request.session['living_with_dependents'] = False
        # Create and save a new Registration object
        if name:
            data.user=user
            data.email=email
            data.name=name
            data.gender=gender
            data.dob=dob
            data.relationship=relationship
            data.occupation=occupation
            data.school_name=school_name
            data.grade=grade
            data.job_name=job_name
            data.job_company=job_company
            data.job_details=job_details
            data.company_name=company_name
            data.business_type=business_type
            data.company_details=company_details
            data.buisness_details=buisness_details
            data.passport_number=passport_number
            data.passport_expiry=passport_expiry
            data.nationality=nationality
            data.proof_of_origin=proof_of_origin
            data.origin_id_number=origin_id_number
            data.visa_status=visa_status
            data.visa_document=visa_document
            data.passport_picture=profile_pic
            data.visa_expiry_date=visa_expiry_date
            data.staying_in_rwanda_since=staying_in_rwanda_since
            data.living_with_dependents=living_with_dependents
            data.save()
            return redirect('step-2')


    return HttpResponse('error')


def step2(request):
    user = request.user
    data = Registration.objects.get(user=user)
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        whatsapp_number = request.POST.get('whatsapp_number')
        address_in_rwanda = request.POST.get('address_in_rwanda')
        province = request.POST.get('province')
        district = request.POST.get('district')
        sector = request.POST.get('sector')
        cell = request.POST.get('cell')
        if mobile_number:
            data.mobile_number=mobile_number
            data.whatsapp_number=whatsapp_number
            data.address_in_rwanda=address_in_rwanda
            data.province=province
            data.district=district
            data.sector=sector
            data.cell=cell
            data.save()
        print(data)


        return redirect('/step-3/')  # Redirect to a success page

    return render(request, 'form2.html')


def step3(request):
    user = request.user
    data = Registration.objects.get(user=user)
    if request.method == 'POST':
        country = request.POST.get('country')
        address = request.POST.get('address')
        contact_name = request.POST.get('contact_name')
        relation = request.POST.get('relation')
        contact_mobile = request.POST.get('contact_mobile')
        if contact_mobile:
            data.emergency_country = country
            data.other_full_address = address
            data.contact_name = contact_name
            data.relation = relation
            data.emergency_mobile_number = contact_mobile
            data.save()
        # Create a new Registration instance with the provided data
        living_with_dependents = request.session.get('living_with_dependents')
        if living_with_dependents==True:
            return redirect('/step-5/') # Redirect to a success page after saving
        else:
            return redirect('/step-4/')

    return render(request, 'form3.html')

def step4(request):
    user = request.user
    data = Registration.objects.get(user=user)
    if request.method == 'POST':
        attachment1 = request.POST.get('attachment1')
        attachment2 = request.POST.get('attachment2')
        attachment3 = request.POST.get('attachment3')
        attachment4 = request.POST.get('attachment4')
        if attachment1:
            data.attachment1 = attachment1
            data.attachment2 = attachment2
            data.attachment3 = attachment3
            data.attachment4 = attachment4
            data.save()
        # Create a new Registration instance with the provided data

        return redirect('/status/') # Redirect to a success page after saving

    return render(request, 'form4.html')
from .models import Dependent
def add_dependent(request):
    if request.method == 'POST':
        # Retrieve data from the form
        user = request.user
        registration  = Registration.objects.get(user=user)
        name = request.POST.get('name')
        nationality = request.POST.get('nationality')
        occupation = request.POST.get('occupation')
        company = request.POST.get('company')
        company_job = request.POST.get('company_job')
        # Retrieve other fields in a similar way

        # Create a new Dependent object and save it to the database
        dependent = Dependent(
            name=name,
            nationality=nationality,
            occupation=occupation,
            company=company,
            company_job=company_job,
            registration=registration,
            # Set other fields in a similar way
        )
        dependent.save()

        # Redirect to a success page or render a success message
        return redirect('/step-4/')  # Replace 'success' with the URL or view name for success

    return render(request, 'form5.html')
