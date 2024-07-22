from django.contrib import admin
from .models import CSVData,UploadedFile
# Register your models here.
admin.site.register(CSVData)
admin.site.register(UploadedFile)