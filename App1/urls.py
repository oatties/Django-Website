from django.urls import path
from .views import *  #import view.py functions from same level directory

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", Home,name="home"), #call defined view 
    path("blogs", Posts, name="post"), #call defined view
    path('blog/<slug:slug>', PostDetail, name='post-detail'), #call detined view
    path("product", Product,name="product"), #call defined view
    path("case_register",Case,name="case_register") , #call defined view
    path("tracking_input", FillTracking,name="tracking_input"), #call defined view
    path("tracking_db", TrackingDB,name="tracking_db"), #call defined view
    path("tracking", Tracking,name="tracking"), #call defined view
    path("about", AboutUs,name="about-us"), #call defined view
    path("contact", Contact,name="contact"), #call defined view
    path("questions", Questions,name="questions"), #call defined view
    path('remark/<slug:record_id>', Remark,name="remark"), #call defined view  & get parameter <int:record_id> from HTML page -- questions.html
    #Register and Login
    path('register',Register,name='register'),
    path('login',Login ,name='login'),
    path('logout',Logout ,name='logout')
]

urlpatterns  +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)