from django import forms
from .models import Project, Contributer


class ProjectForm(forms.ModelForm):
    """    contributors = forms.ModelMultipleChoiceField(
        queryset=Contributer.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': 5})
    )"""
    class Meta:
        model = Project
        fields = '__all__'
        
class ContributerForm(forms.ModelForm):
    class Meta:
        model = Contributer
        fields = '__all__'
