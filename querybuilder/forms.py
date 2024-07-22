from django import forms
from .models import CSVData

class FileUploadForm(forms.Form):
    file = forms.FileField(label='select a file')
    
class CSVDataFilterForm(forms.Form):
    keyword = forms.CharField(max_length=255, required=False)
    industry = forms.ChoiceField(choices=[], required=False)
    year_founded = forms.ChoiceField(choices=[], required=False)
    locality = forms.ChoiceField(choices=[], required=False)
    country = forms.ChoiceField(choices=[], required=False)
    current_employee_estimate = forms.ChoiceField(choices=[], required=False)
    total_employee_estimate = forms.ChoiceField(choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['industry'].choices = self.get_choices('industry')
        self.fields['year_founded'].choices = self.get_choices('year_founded')
        self.fields['locality'].choices = self.get_choices('locality')
        self.fields['country'].choices = self.get_choices('country')
        self.fields['current_employee_estimate'].choices = self.get_choices('current_employee_estimate')
        self.fields['total_employee_estimate'].choices = self.get_choices('total_employee_estimate')

    def get_choices(self, field_name):
        choices = CSVData.objects.values_list(field_name, flat=True).distinct()
        choices1 = []
        for choice in choices:
            if choice and choice.lower() != 'nan':
                choices1.append(choice)
        choices1.sort()
        return [('', 'All')] + [(choice, choice) for choice in choices1]
