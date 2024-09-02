from django import forms
from .models import Project, Contributer, ContributorProjectContribution, ContributerTechnology, Technology


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image',
                  'github_link', 'technologies']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class ContributerForm(forms.ModelForm):
    class Meta:
        model = Contributer
        fields = ['name', 'image',
                  'email', 'github_link', 'linkedin_link']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
    

class ContributerTechnologyForm(forms.ModelForm):
    class Meta:
        model = ContributerTechnology
        fields = ['technology', 'level']

    def __init__(self, *args, **kwargs):
        self.contributer = kwargs.pop('contributer', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        technology = cleaned_data.get('technology')
        if technology and self.contributer:
            existing_instance = ContributerTechnology.objects.filter(
                contributer=self.contributer, technology=technology
            ).exists()
            if existing_instance:
                raise forms.ValidationError(
                    'The contributer already has this technology.')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.contributer:
            instance.contributer = self.contributer
        if commit:
            instance.save()
        return instance

class ContributionForm(forms.ModelForm):
    class Meta:
        model = ContributorProjectContribution
        fields = ['contributor', 'contribution']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
    
class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['technology']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
