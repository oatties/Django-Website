from django.contrib import admin
# from .models import TrackingInfo,CaseInfo
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
#admin.site.register(<models>)
admin.site.register(TrackingInfo)
admin.site.register(CaseInfo)
admin.site.register(Author)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields       =   ("body"),
    list_display            =   ["id", "title", "images"]
    list_editable           =   ["title"]

admin.site.register(Post, PostAdmin)
