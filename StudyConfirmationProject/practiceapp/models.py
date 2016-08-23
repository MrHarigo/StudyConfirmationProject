from datetime import timezone

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Certificate(models.Model):
    certificate_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.certificate_text


class RequestManager(models.Manager):
    def create_request(self, certificate, group, name, surname, father_name, amount):
        request = self.create(certificate=certificate, group=group, name=name, surname=surname, father_name=father_name, amount=amount, pub_date= timezone.now())
        return request


class Request(models.Model):
    certificate = models.ForeignKey(Certificate)
    group = models.CharField(max_length=10)
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    fathername = models.CharField(max_length=20)
    amount = models.IntegerField(default=1)
    pub_date = models.DateTimeField('date published')

    objects = RequestManager()

    def __str__(self):
        return self.surname


class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'

class MySiteProfile(models.Model):
    user = models.OneToOneField(User)
    father_name = models.CharField(max_length=20)
    group = models.CharField(max_length=20)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'