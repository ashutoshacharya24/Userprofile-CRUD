# UserProfile-CRUD
 CRUD operation in userDatabase using django ``Form`` and ``DTL``
 
form.py
```from django import forms
from .models import User
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'userName':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phoneNumber':forms.NumberInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'comment':forms.TextInput(attrs={'class':'form-control'}),
            
        }```
