from django import forms
from . models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label='Select position'  #this sets the doted line dropdown option to 'Select position' as its label name 
        self.fields['email'].required = False      #sets the Email field filling to optional in the form

        
