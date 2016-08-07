from django import forms

class ContactForm(forms.Form):
    group = forms.CharField(max_length=10)
    surname = forms.CharField(max_length=25)
    name = forms.CharField(max_length=20)
    father_name = forms.CharField(max_length=25)
    amount = forms.IntegerField()