from django.db import models

# Create your models here.

class Deptmnt(models.Model):
    dep_name=models.CharField(max_length=20)
    dep_description=models.TextField()
    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Deptmnt,on_delete=models.CASCADE)
    doc_img=models.ImageField(upload_to='doctors')

    def __str__(self):
        return self.doc_name



class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=255)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)


class Contact(models.Model):
    c_name=models.CharField(max_length=255)
    c_phone=models.CharField(max_length=255)
    c_email=models.EmailField()
    c_department=models.CharField(max_length=255)
    def __str__(self):
        return self.c_name


    
