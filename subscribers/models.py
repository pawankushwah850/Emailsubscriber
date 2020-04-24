from django.db import models

from django.forms import ModelForm,EmailInput,Textarea

# Create your models here.

class UserEmail(models.Model):

    Email=models.EmailField(max_length=100)

    def __str__(self):
        return self.Email

class subscriberForm(ModelForm):
    """ creatinf form , which we show in our templates, here widgets is using to applying bootstrap in form"""
    class Meta:
        model=UserEmail
        fields=('Email',)
        widgets = {
            'Email': EmailInput(attrs={'class':'form-control w-75'}),
        }


