from django.contrib import admin
from .models import Certificate, Question
# Register your models here.

class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 6


class CertificateAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]

admin.site.register(Certificate, CertificateAdmin)