from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
from smartattend.models import StudentDetails
from django.db import connection
from smartattend.models import Presentees
# Create your views here.
name=''
rno=''
mail=''
sem=''
city=''
em=''
pwd=''
"""def smartpage(request):
    global name,rno,mail,sem,city
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='student')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                name=value
            if key=="Rollno":
                rno=value
            if key=="MailId":
                mail=value
            if key=="Semester":
                sem=value
            if key=="City":
                city=value
        c="insert into studentdata Values('{}','{}','{}','{}','{}')".format(name,rno,mail,sem,city)
        cursor.execute(c)
        m.commit()
    return render(request,"student_rege.html")"""



# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='student')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from login where username='{}' and pasword='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
           messages.error(request,'Invalid Details')
        else:
            return render(request,'dashboard.html')

    return render(request,'login.html')



def StudentRege(request):
    global name,rno,mail,sem,city
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='student')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                name=value
            if key=="Rollno":
                rno=value
            if key=="MailId":
                mail=value
            if key=="Semester":
                sem=value
            if key=="City":
                city=value
        c="insert into studentdata Values('{}','{}','{}','{}','{}','{}')".format('',name,rno,mail,sem,city)
        cursor.execute(c)
        m.commit()
    return render(request,"student_rege.html")



    

def dash(request):
    return render(request,'dashboard.html')
            
def admin(request):
    return render(request,'admin.html')

def totalStudents(request):
    resultsdisplay=StudentDetails.objects.all()
    return render(request,'totalStudents.html',{'StudentDetails': resultsdisplay})
    

def Presentees(request):
    cursor=connection.cursor()
    cursor.execute("select studentdata.name,studentdata.rollno,studentdata.sem,smartattend.date from studentdata join smartattend on studentdata.name=smartattend.name")
    results=cursor.fetchall()
    return render(request,'Presentees.html',{'Presentees':results})

def Absentees(request):
    cursor1=connection.cursor()
    cursor1.execute("select studentdata.name,studentdata.rollno,studentdata.sem,smartattend.date from studentdata join smartattend on smartattend.name!=studentdata.name")
    results=cursor1.fetchall()
    return render(request,'Absentees.html')

def Attendence(request):
    return render(request,'Attendence.html')





    


