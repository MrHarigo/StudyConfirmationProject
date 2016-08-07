from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Certificate(models.Model):
    #group = models.CharField(max_length=10)
    #surname = models.CharField(max_length=20)
    #name = models.CharField(max_length=10)
    #fathername = models.CharField(max_length=20)
    certificate_text = models.CharField(max_length=200)
    #amount = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.certificate_text

class Question(models.Model):
    certificate = models.ForeignKey(Certificate)
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.question_text

class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'

class MySiteProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    group = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    lucky_number = models.IntegerField()