from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from .models import ContactMessage , TrackingInfo, CaseInfo
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required #บังคับให้ login
from django.contrib.auth.models import User    #Do authentication
from django.contrib.auth import authenticate, login, logout  #for login authentication
from django.core import exceptions


# Create your views here.
#M T V ( Models Templates Views)

#--HOME--#
def Home(request):    #View name
    return render(request,"myapp/home.html")   #Open HTML file under template folder

# #--Blog--#
# def Blog(request):  #View name
#     return render(request, "myapp/blog.html")    #Open HTML file under template folder  

#--Post--#
def Posts(request):
    posts = Post.objects.all().order_by('id').reverse()[:5] #get 3 latest items from table in db
    context = {'posts':posts}

    return render(request,'myapp/blogs.html',context)

#--Post Details--#   ********Slug
def PostDetail(request, slug):

    nav_posts = Post.objects.all() .order_by('id').reverse ()[:3] #get 3 latest items from table in db

    try:
        single_post = get_object_or_404(Post, slug=slug)
        print("content detail!! -", single_post)
            
    except Post.DoesNotExist:
         return render(request, 'myapp/home.html')

    context = {'single_post':single_post,
               'nav_posts': nav_posts    
               }

    return render(request,'myapp/blog-detail.html',context)


#--Product--#
def Product(request):    #View name
    return render(request,"myapp/product.html")   #Open HTML file under template folder  

#--Case--#
def Case(request):
    context = {} #return variable to html
    if request.method == "POST":
        status = ""

        #Get submitted data
        input_data = request.POST.copy()
        fname = input_data.get("case_fname")
        lname = input_data.get("case_lname")
        bd    = input_data.get("case_bd")
        addr  = input_data.get("case_addr")
        tel   = input_data.get("case_tel")

        """     
        #################################################################   
            #Data Validation
            if fname.strip() == "" or lname.strip() == "" or bd.strip() == "" or addr.strip() == "" or tel.strip() == "":  
                status                  = "Error"    
                context["status"]       = status        
                context["status_msg"]   = "Please fill in all data."

            if  status == "Error":
                return render(request,"myapp/case_register.html",context)
        #################################################################       
        """ 

        print(input_data)
        row = CaseInfo() #create structure to store data of Case

        row.fname   =   fname
        row.lname   =   lname
        row.bdate   =   bd    
        row.addr    =   addr 
        row.tel     =   tel
        row.save()

        #set return status to html
        context["status"]       =   "Success"
        context["status_msg"]   =   "Data was added to Database"        
        
    return render(request,"myapp/case_register.html",context)


#--FillTracking--#
def FillTracking(request):    #View name

    context = {} #return variables to html
    context["tracking_status"] =    {   '00': '00 -  รับทราบคำสั่งซื้อ',
                                        '10': '10 -  บรรจุสินค้า',
                                        '20': '20 -  รอขนส่งมารับ' ,
                                        '30': '30 -  อยู่ระหว่างขนส่ง' ,
                                        '40': '40 - ถึงสถานีกระจายสินค้าปลายทาง' ,
                                        '50': '50 -  ออกนำส่งให้ผู้รับ' ,
                                        '60': '60 -  ส่งสำเร็จ',
                                        '70': '70 -  ส่งไม่สำเร็จ' ,
                                        '80': '80 -  ยกเลิกคำสั่งซื้อ'
                                    }
    #If "POST" -- submit data
    if request.method == "POST":

            status                  = ""

            #Get submitted data
            input_data = request.POST.copy() 
            tracking_id = input_data.get("tracking_id")
            cust_name   = input_data.get("cust_name")
            tracking_status      = input_data.get("tracking_status")


          #################################################################   
            #Data Validation
            if tracking_id.strip() == "" or cust_name.strip() == "":  
                status                  = "Error"    
                context["status"]       = status        
                context["status_msg"]   = "Please fill in all data."

            if  status == "Error":
                return render(request,"myapp/tracking_input.html",context)
          #################################################################                  

            print(input_data)
            #save record to DB table    
            row = TrackingInfo() #create structure to store data of tracking
            row.tracking_id =   tracking_id
            row.cust_name   =   cust_name
            row.status      =   tracking_status
            row.save()

            #set return status to html
            context["status"]       =   "Success"
            context["status_msg"]   =   "Data was added to Database"

    return render(request,"myapp/tracking_input.html",context)   #Open HTML file under template folder      


#--Tracking--#
def TrackingDB(request):    #View name
    #Tracking list
    trackingList =  TrackingInfo.objects.all()
    context = {"tracking_list": trackingList} #response var & msg return to View 

    return render(request,"myapp/tracking_db.html",context)   #Open HTML file under template folder    


#--Tracking--#
def Tracking(request):    #View name
    #Tracking list
    trackingList = [    {'id':'TH012345E001','name':'Bigon','status':'02'},
                        {'id':'TH012345E002','name':'Nguyen','status':'03'},
                        {'id':'TH012345E003','name':'Takedo','status':'00'},
                    ]
    context = {"tracking_list": trackingList} #response var & msg return to View 

    #print(context)
    return render(request,"myapp/tracking.html",context)   #Open HTML file under template folder    

#--AboutUs--#
def AboutUs(request):    #View name
    return render(request,"myapp/aboutus.html")   #Open HTML file under template folder

#--Contact--#
def Contact(request):    #View name

    context = {} #response var & msg return to View 

    if request.method == "POST":
        data = request.POST.copy()
        title = data.get("title")   #from HTML tag name = title
        email = data.get("email")   #from HTML tag name = email
        detail = data.get("detial")
        #print(title,email,detail) #test printing

        if title == "" :
            context["status"]='Error'        
            return render(request,"myapp/contact.html",context)   #Open HTML file under template folder    

        
        #save record to DB table
        record = ContactMessage()  #create structure to store data
        #store data
        record.title = title
        record.email = email
        record.detail = detail
        #add record to DB
        record.save()
        context["status"] = "Success"

    return render(request,"myapp/contact.html",context)   #Open HTML file under template folder    

#--Questions--#
@login_required ####required login with function decorators
def Questions(request):    #View name
    #Tracking list
    questions =  TrackingInfo.objects.all()
    context = {"questions": questions} #response var & msg return to View 

    return render(request,"myapp/questions.html",context)   #Open HTML file under template folder    


#--Submit Remark--#
@login_required
def Remark(request,record_id):    #View name with parameter from urls.py file
#localhost:8000/remark/record_id


    context = {} #return variables to html

    

    #Get data from DB
    row = TrackingInfo.objects.get(tracking_id=record_id)
                                    
    #If "POST" -- submit data
    if request.method == "POST":

            status                  = ""

            #Get submitted data           
            input_data  = request.POST.copy() 
            remark      = input_data.get("remark")

          #################################################################   
            #Data Validation
            if remark.strip() == "" :  
                status                  = "Error"    
                context["status"]       = status        
                context["status_msg"]   = "Please fill remark."

            if  status == "Error":
                return render(request,"myapp/remark.html",context)
          #################################################################                  

            print(input_data)
            row.remark  = remark    #set submit data to record
            row.save()              #update record data

            #set return status to html
            context["status"]       =   "Success"
            context["status_msg"]   =   "Remark data was updated"
            
    context["row"]          =   row

    return render(request,"myapp/remark.html",context)   #Open HTML file under template folder     

def Register(request):

    context = {}

    #If "POST" -- submit data
    if request.method == "POST":
        data        = request.POST.copy()
        firstname   = data.get('firstname')
        lastname    = data.get('lastname')
        email       = data.get('email')
        password    = data.get('pwd')

        # Query the database to check if the item already exists
        # exists = User.objects.filter(username = email).exists()
        # print("EXIST:",exists)
        if User.objects.filter(username = email).exists():
            # raise exceptions.ValidationError(f"This user '{email}' already exists")
            status  =   "Error"
            msg     =   f"User '{email}' already exists."
            context = { 'status'        : status,
                        'status_msg'    : msg,
                        }      
        else:
        #Create User
            newuser     = User() 
            newuser.username    = email
            newuser.email       = email
            newuser.first_name  = firstname
            newuser.last_name   = lastname
            newuser.set_password(password)
            newuser.save()

            status  =   "Success"
            msg     =   "You have successfully registered."

            context = { 'status'        : status,
                        'status_msg'    : msg,
                        }

    return render(request,'myapp/register.html',context) 



def Login(request):

    context = {}

    #If "POST" -- submit data
    if request.method == "POST":
        data        = request.POST.copy()
        email       = data.get('email')
        password    = data.get('pwd')


        # Query the database to check if the item doesn't exists
        if not User.objects.filter(username = email).exists():

            # raise exceptions.ValidationError(f"This user '{email}' already exists")
            status  =   "Error"
            msg     =   f"User '{email}' doesn't exists."
            context = { 'status'        : status,
                        'status_msg'    : msg,
                        'nouser'        : "no user"
                        }      
        else:

            #Authenticate
            user    = authenticate(request, username = email,password=password)
            # print(user)
            if user is not None:
                login(request,user)
                # print("login complete")
                return redirect("questions")   #redirect to target page
            else:
                # messages.error(request, 'Invalid username or password.')

                status  =   "Error"
                msg     =   f"Incorrect password."
                context = { 'status'        : status,
                            'status_msg'    : msg,
                            'incorrectpwd'  : "Incorrect password"
                            }                    

    return render(request,'myapp/login.html',context) 

def Logout(request):

    logout(request)
    # Redirect to a logged out page or any other page
    return redirect('home')

