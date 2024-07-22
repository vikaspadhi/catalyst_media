from rest_framework import serializers
from .models import CSVData

class CSVDataFilterSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=255, required=False, allow_blank=True)
    industry = serializers.ChoiceField(choices=[], required=False, allow_blank=True)
    year_founded = serializers.ChoiceField(choices=[], required=False, allow_blank=True)
    locality = serializers.ChoiceField(choices=[], required=False, allow_blank=True)
    country = serializers.ChoiceField(choices=[], required=False, allow_blank=True)
    current_employee_estimate = serializers.ChoiceField(choices=[], required=False, allow_blank=True)
    total_employee_estimate = serializers.ChoiceField(choices=[], required=False, allow_blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['industry'].choices = self.get_sorted_choices('industry')
        self.fields['year_founded'].choices = self.get_sorted_choices('year_founded')
        self.fields['locality'].choices = self.get_sorted_choices('locality')
        self.fields['country'].choices = self.get_sorted_choices('country')
        self.fields['current_employee_estimate'].choices = self.get_sorted_choices('current_employee_estimate')
        self.fields['total_employee_estimate'].choices = self.get_sorted_choices('total_employee_estimate')

    def get_sorted_choices(self, field_name):
        choices = CSVData.objects.values_list(field_name, flat=True).distinct()
        choices = [choice for choice in choices if choice and choice.lower() != 'nan']
        choices.sort()
        return [('', 'All')] + [(choice, choice) for choice in choices]
