from django.core.mail import EmailMultiAlternatives 
from django.template.loader import render_to_string 
import smtplib


def orderinfo_email(menu_item,item_cost,your_name,your_email,your_mobile,order_date,receiver):
    subject = 'A preorder has been placed!'
    sender = 'davinci.monalissa@gmail.com'

    text_content = render_to_string('email/preorder.txt',{"menu":menu_item,"cost":item_cost,"email":your_email,"mobile":your_mobile,"name":your_name,"date":order_date})
    html_content = render_to_string('email/preorder.html',{"menu":menu_item,"cost":item_cost,"name":your_name,"email":your_email,"mobile":your_mobile,"date":order_date})
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