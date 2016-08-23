from django import forms

class ContactForm(forms.Form):
    group = forms.CharField(max_length=10, label='Ваша группа')
    surname = forms.CharField(max_length=25, label='Фамилия')
    name = forms.CharField(max_length=20, label='Имя')
    father_name = forms.CharField(max_length=25, label='Отчество')
    amount = forms.IntegerField(label='Количество экземпляров')