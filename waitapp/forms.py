from .models import TruckDriver
from django import forms


STATUS_CHOICES = [
    ('Waiting', 'Waiting'),
    ('In Progress', 'In Progress'),
    ('Finished', 'Finished'),
    ('','-')
]

class TruckDriverForm(forms.ModelForm):
    class Meta:
        model = TruckDriver
        fields = ['name', 'truck_number', 'company']
    name = forms.CharField(label='Driver Name', max_length=200,required=True)
    truck_number = forms.CharField(label='Truck Number', max_length=200,required=True)
    company = forms.CharField(label='Company', max_length=200,required=True)
    
class MasterReportForm(forms.Form):
    status = forms.CharField(label='Status', required=False, max_length=200)
