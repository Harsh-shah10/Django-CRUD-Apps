from dataclasses import field
from django.forms import ModelForm
from .models import Project,Contactus


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title','description','demo_link','source_link','tags']

class ContactusForm(ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'
        