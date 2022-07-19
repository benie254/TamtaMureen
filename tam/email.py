from django.core.mail import EmailMultiAlternatives 
from django.template.loader import render_to_string 


def orderinfo_email(name,receiver):
    subject = 'A preorder has been placed!'
    sender = 'davincibenie@gmail.com'

    text_content = render_to_string('email/preorder.txt',{"name":name})
    html_content = render_to_string('email/preorder.html',{"name":name})
    message = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    message.attach_alternative(html_content,'text/html')
    message.send()