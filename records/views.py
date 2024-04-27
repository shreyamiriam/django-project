from django.shortcuts import render
from .models import Deptmnt,Doctors,Contact
from .forms import BookingForm

# Create your views here.

def index(request):
    return render(request,"index.html")
def contact(request):
    dict_contact={
        'contactkey':Contact.objects.all()
    }
    return render(request,"contact.html",dict_contact)
def departments(request):
    dict_dept={
        'deptkey':Deptmnt.objects.all()
    }
    return render(request,"department.html",dict_dept)
def about(request):
    return render(request,"about.html")

def booking(request):
    if request.method=="POST":
        formdemo=BookingForm(request.POST)
        if formdemo.is_valid():
            formdemo.save()
        return render(request,'c.html')

    myform1=BookingForm()
    dict_book={
        'formkey':myform1
    }
    return render(request,"booking.html",dict_book)
def doctors(request):
    dict_docs={
        'doctkey':Doctors.objects.all()
    }

    return render(request,"doctors.html",dict_docs)