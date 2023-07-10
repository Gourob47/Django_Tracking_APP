from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.conf import  settings
from Home.models import Employee
from Home.models import Monitor

# Create your views here.

#Company Signup 
def signupCompany(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        

        my_user=User.objects.create_user(email,name,password)
        my_user.save()
        return redirect('/login')
         
    return render(request,'signup.html')


#Company Login
def loginCompany(request):
    if request.method=='POST':
        username = request.POST["email"]
        password = request.POST["password"]
        

        user=authenticate(request,username=username,password=password)
   
        if user is not None:
            login(request, user)
            return redirect('home')
        else:       
            return redirect('/login')
    
    return render(request,'login.html')     


#Home Page after Login
def home(request):
      print(request.user.is_authenticated)
      if not request.user.is_authenticated:
          return redirect('/login')
      else:
            #Create Multiple Employee
            if request.method=='POST':
              em_name = request.POST["name"]     
              new= Employee.objects.create(employee_name=em_name,user=request.user)
              new.save()

            #Filtering Loggedin Company's Employee       
            com_employee=Employee.objects.filter(user=request.user)
            
            context={'employee':com_employee}
            
            return render(request,'home.html',context)
          
 
 
def employ(request,id):
         if not request.user.is_authenticated:
            return redirect('/login')
         else:
                #First, Filtering Loggedin Company's DataSet
                userholder=Monitor.objects.filter(user=request.user)
                #Then,Filtering use history of signgle Employee
                access=userholder.filter(employee_name=id)
                
                context={'monitor':access,'id':id}  
                return render(request, 'employ.html',context)
      

 
def accessories(request,id):
        if not request.user.is_authenticated:
            return redirect('/login')
         #First, Filtering Loggedin Company's Employee for Select Employee       
        com_employee=Employee.objects.filter(user=request.user)
        
        if request.method=='POST':
             employee_name = request.POST["name"] 
             accessories_id = id           
             checkoutTime = request.POST["checkout"] 
             returnTime = request.POST["return"] 

             #checkout Time must be less than Return Time
             #If every validation ok, Then New Monitor create in Database
             #Here uses only One table for Employee uses and Device Monitoring like key value pairs
             if(checkoutTime<returnTime):
                new=Monitor.objects.create(user=request.user,employee_name=employee_name,accessories_id=accessories_id,checkout_Time=checkoutTime, return_Time=returnTime)
             

        #Then, Filtering Loggedin Company's Dataset
        userholder=Monitor.objects.filter(user=request.user)
        #Finally,Filtering Employee for monitor by Device
        user=userholder.filter(accessories_id=id)
      
        context={'employee':com_employee,'monitor':user,'id':id}  
        return render(request, 'accessories.html',context)

#Company Logout
def logoutCompany(request):
         logout(request)
         return redirect('/login') 
    
   

      
      
            
       

     
       