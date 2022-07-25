from django.core.mail import EmailMultiAlternatives 
from django.template.loader import render_to_string 
import smtplib


def orderinfo_email(your_name,order_date,receiver):
    subject = 'A preorder has been placed!'
    sender = 'davinci.monalissa@gmail.com'

    text_content = render_to_string('email/preorder.txt',{"name":your_name,"date":order_date})
    html_content = render_to_string('email/preorder.html',{"name":your_name,"date":order_date})
    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def contact_email(name,email,message,receiver):
    subject = 'You have a new message!'
    sender = 'davinci.monalissa@gmail.com'

    text_content = render_to_string('email/contact.txt',{"name":name,"email":email,"message":message})
    html_content = render_to_string('email/contact.html',{"name":name,"email":email,"message":message})
    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()