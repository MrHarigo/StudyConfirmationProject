from django import forms

class ContactForm(forms.Form):
    amount = forms.IntegerField(label='Количество экземпляров')