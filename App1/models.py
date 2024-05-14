#these models will be created in DB as table with command line 'python manage.py makemigrations'
#after check the result from prior step type 'python manage.py migrate' to update DB
from django.db import models
from taggit.managers import TaggableManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class ContactMessage(models.Model):
    #Declare Fields
    title   = models.CharField(max_length=20)
    email   = models.CharField(max_length=100)
    detail  = models.TextField(blank=True, null =True)
    reply   = models.BooleanField(default=False)

    def __str__(self):   #return text after call class *also show as item text in DB table item
        return self.title 

class TrackingInfo(models.Model):

    lStatus = [     ( '00', '00 -  รับทราบคำสั่งซื้อ'),
                    ( '10', '10 -  บรรจุสินค้า'),
                    ( '20', '20 -  รอขนส่งมารับ'), 
                    ( '30', '30 -  อยู่ระหว่างขนส่ง'), 
                    ( '40', '40 - ถึงสถานีกระจายสินค้าปลายทาง'), 
                    ( '50', '50 -  ออกนำส่งให้ผู้รับ'), 
                    ( '60', '60 -  ส่งสำเร็จ'),
                    ( '70', '70 -  ส่งไม่สำเร็จ'), 
                    ( '80', '80 -  ยกเลิกคำสั่งซื้อ')
                ]       

    tracking_id =   models.CharField(max_length=12, blank=False,  primary_key=True)
    cust_name   =   models.CharField(max_length=200, blank=False)
    status      =   models.TextField(choices=lStatus, blank=False, default= lStatus[0])  #Drop down list value
    remark      =   models.TextField(null=True, blank=True, verbose_name="Remark")

    def __str__(self):
        return self.tracking_id + "     " + self.cust_name + "      " + self.status

class CaseInfo(models.Model):
    #Declare fields
    fname = models.CharField(max_length=100) 
    lname = models.CharField(max_length=100)
    bdate = models.DateField()
    addr  = models.TextField()
    tel   = PhoneNumberField(blank=True)

    def __str__(self):
        return ("{} - {}".format(self.fname,self.bdate))
    
##Model for Blog page -START    
class Author(models.Model):
    author_name     =   models.CharField(max_length=100)
    image           =   models.ImageField(upload_to="author-images/", blank=True, null=True, default="default.png")

    def __str__(self):
        return self.author_name
    
class Post(models.Model):
    author          =   models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)  #using with Foreign Key
    title           =   models.CharField(max_length=200)
    description     =   models.TextField(max_length=280, null=True, blank=True)
    body            =   models.TextField(null=True, blank=True)
    images          =   models.ImageField(upload_to="post-images/", null=True, blank=True)
    created_date    =   models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_date   =   models.DateTimeField(auto_now=True)
    slug            =   models.SlugField(unique=True, max_length=180, null=True, blank=True)
    tags            =   TaggableManager()  #Taggit Module

    def __str__(self):
        return self.title

##Model for Blog page -END    