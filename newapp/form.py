from django import forms
from newapp.models import User
from django.contrib.auth.models import User
from newapp.models import addemployee1
from newapp.models import addstudent1

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'


class addemployee2(forms.ModelForm):
    class Meta:
        model=addemployee1
        fields='__all__'

        
class addstudent2(forms.ModelForm):
    class Meta:
        model=addstudent1
        fields='__all__'