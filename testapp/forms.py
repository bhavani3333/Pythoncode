from django import forms

class registration(forms.Form):
    fistname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    degree = forms.Charfield()
    education = forms.CharField()
    address = forms.CharField()

    
   