from django.shortcuts import render
from subscribers.models import subscriberForm
from subscribe.settings import EMAIL_HOST_USER 
from django.core.mail import send_mail,BadHeaderError
# Create your views here.

def index(request):
    form=subscriberForm()
    return render(request,"index.html",{"form":form})

def subscribe(request):

    if request.method=="GET":
        form=subscriberForm(request.GET)

        if form.is_valid():
            """ saving data in our database """
            form.save()

            """ using this cleaned data must, to get value of email"""

            senderEmail=form.cleaned_data['Email']

            subject="Welcome to "+senderEmail

            """here your message will be, also you send templates etc"""

            message="Thanking you for subscribing me, you get every updates within a seconds..."

            """ receiver email address"""
            
            recipient=str(senderEmail)

            if subject and message and recipient :
                try:
                    
                    """ send email is function in django to use this to send mail"""
                    """ if you want send bulk email add more email in [recipients]"""


                    send_mail(subject,message,EMAIL_HOST_USER,[recipient],fail_silently=False)
                except BadHeaderError :

                    """ bad header error means prevent from header injection apply by hackers"""

                    return render(request,"subscribe.html",{'message':'Invalid header found.','class':'text-danger'})

                return render(request,"subscribe.html",{'message':'Thanking you For Subscribing..','class':'text-success'})

    return render(request,"subscribe.html",{"message":"Make sure all fields are entered and valid.",'class':'text-info'})