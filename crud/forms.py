from cProfile import label
from dataclasses import field
from django import forms 
from .models import Project, Developer


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['project_id']
        label = {
            'name': 'Project Name',
            'description': 'Description',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'cost': 'Cost',
            'developers': 'Developer'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control'}),
            'end_date': forms.DateInput(attrs={'class':'form-control'}),
            'cost': forms.NumberInput(attrs={'class':'form-control'}),
            'developer': forms.Select(attrs={'class':'form-control'}),
         }

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        field = ('first_name', 'last_name', 'projects', 'language')
        exclude = ['developer_id']
        label = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'projects': 'Project',
            'language': 'Language'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'project': forms.Select(attrs={'class':'form-control'}),
            'language': forms.Select(attrs={'class':'form-control'}),
        }
        
