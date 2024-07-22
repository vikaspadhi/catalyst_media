from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import FileUploadForm , CSVDataFilterForm
from django.http import JsonResponse
from django.core.files.storage import default_storage
from .models import UploadedFile, CSVData
import os
import pandas as pd
import threading
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import CSVDataFilterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse_lazy

# Create your views here.
class UsersList(LoginRequiredMixin ,ListView):
    model=User
    template_name='querybuilder/users.html'
    context_object_name = 'users'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = self.request.session.pop('custom_message', None)
        return context
    


    

class UploadData(LoginRequiredMixin , FormView):
    form_class = FileUploadForm
    template_name = 'querybuilder/upload.html'
    
    def post(self, request, *args, **kwargs):
        chunk_number = int(request.POST['chunkNumber'])
        total_chunks = int(request.POST['totalChunks'])
        file = request.FILES['file']
        file_name = file.name.split('.part_')[0]
        file_path = os.path.join('uploads', file_name)
        # Append chunk to the file
        with default_storage.open(file_path, 'ab') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Respond with success if this is the last chunk
        if chunk_number == total_chunks - 1:
            # Save the UploadedFile instance
            uploaded_file = UploadedFile.objects.create(file=file_path)
            # Parse the CSV and save data to the database
            threading.Thread(self.parse_and_save_csv(file_path, uploaded_file))
            return JsonResponse({'status': 'completed'}, status=200)
        else:
            return JsonResponse({'status': 'partially_completed'}, status=200)

    def parse_and_save_csv(self, file_path, uploaded_file):
        # Read the CSV file
        print(f'====================={file_path}=========================')
        df = pd.read_csv(f'media/{file_path}')
        
        
        for _, row in df.iterrows():
            CSVData.objects.create(
                com_id=row['company id'],
                name=row['name'],
                domain=row['domain'],
                year_founded=row['year founded'],
                industry=row['industry'],
                size_range=row['size range'],
                locality=row['locality'],
                country=row['country'],
                linkedin_url=row['linkedin url'],
                current_employee_estimate=row['current employee estimate'],
                total_employee_estimate=row['total employee estimate'],
                
                uploaded_file=uploaded_file
            )
    
    

class QueryBuilder(LoginRequiredMixin,FormView):
    template_name = 'querybuilder/query.html'
    form_class = CSVDataFilterForm
    success_url = reverse_lazy('query')
    
    
class CSVDataFilterAPIView(APIView):    
    def post(self, request, *args, **kwargs):
        serializer = CSVDataFilterSerializer(data=request.data)
        if serializer.is_valid():
            filters = {k: v for k, v in serializer.validated_data.items() if v and k != 'keyword'}
            keyword = serializer.validated_data.get('keyword', '')
            if keyword:
                filters['name__icontains'] = keyword
            count = CSVData.objects.filter(**filters).count()
            return Response({'count': count}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
