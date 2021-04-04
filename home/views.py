from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def home(request):
    return render(request, "home.html")

def register(request):

        if request.method == "POST":
            first_name = request.POST['first_name']
            username= request.POST['username']
            email= request.POST['email']
            password= request.POST['password']
            confpassword= request.POST['confpassword']
            
            if password==confpassword:
                if User.objects.filter(username=username).exists():
                    messages.success(request, 'Username is already taken !!')
                elif User.objects.filter(username=username).exists():
                    messages.success(request, 'Email already registered, try with Another Email !!')
                user = User.objects.create_user(first_name=first_name, username=username,email=email, password=password)
                user.save()
                messages.success(request, 'User has been successfully registered !!')
                return redirect('/login')
            else:
                messages.error(request, 'Passwords do not Match !!')
                return render(request, "register.html")
        else:
            return render(request, "register.html")

def login(request):

        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Credentials!!')
                return redirect('/login')

        else:
            return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def add(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        username = request.POST.get('username')
        result = request.POST.get('result')
        docname = request.POST.get('docname')
        meds = request.POST.get('meds')
        contact = Contact(fname = fname, username=username, result=result, docname=docname, meds=meds, date = datetime.today() )
        contact.save()    
        messages.success(request, 'Record has been successfully registered !!')
    return render(request, "add.html")

def doctor(request):
    return render(request, 'doctor.html')


def details(request):
    patientobject = Contact.objects.raw('SELECT id,username,fname,result,meds,docname,date FROM home_contact ORDER BY id ASC')
    return render(request,'details.html', {"data":patientobject})

def docview(request):
     patientobject1 = Contact.objects.raw('SELECT id,username,fname,result,meds,docname,date FROM home_contact ORDER BY id ASC')
     return render (request,'docview.html', {"data":patientobject1})