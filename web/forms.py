from dataclasses import fields
from django.forms import ModelForm, Textarea
from dashboard.models import Family, Addoption

class AddoptionForm(ModelForm):
    class Meta:
        model = Addoption
        exclude = ['approved','family','child']



class FamilyForm(ModelForm):
    class Meta:
        model = Family
        # fields = ['father', 'mother', 'location', 'dependent_children', 'father_phone', 'mother_phone', 'father_email', 'mother_email', 'father_occupation', 'mother_occupation', 'father_occupation_other', 'mother_occupation_other', 'religion']
        fields = '__all__'