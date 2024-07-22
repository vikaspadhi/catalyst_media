from django.db import models

# Create your models here.
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
class CSVData(models.Model):
    com_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    linkedin_url = models.CharField(max_length=255)
    current_employee_estimate = models.CharField(max_length=255)
    total_employee_estimate = models.CharField(max_length=255)
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE, related_name='csv_data')
    
    
    