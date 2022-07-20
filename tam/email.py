from django.core.mail import EmailMultiAlternatives 
from django.template.loader import render_to_string 
import smtplib


def orderinfo_email(name,date,receiver):
    subject = 'A preorder has been placed!'
    sender = 'davinci.monalissa@gmail.com'

    text_content = render_to_string('email/preorder.txt',{"name":name,"date":date})
    html_content = render_to_string('email/preorder.html',{"name":name,"date":date})
    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

    