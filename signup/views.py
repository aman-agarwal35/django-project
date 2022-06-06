from django.shortcuts import render
import mysql.connector as sql
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
import re

firstname= ''
lastname= ''
sex= ''
city=''
state= ''
contact= ''
email= ''
password= ''

# Create your views here.

def signaction(request):
  global firstname, lastname, sex, city, state, contact, email, password

  if request.method == 'POST':
    obj= sql.connect(host= "localhost", user= "root", password= "anisha5409", database= "login")
    cursor= obj.cursor()
    data= request.POST
    for key,value in data.items():
      if key== "first_name":
        firstname= value

      if key== "last_name":
        lastname= value

      if key== "sex":
        sex= value

      if key== "city":
        city= value

      if key== "state":
        state= value

      if key== "contact":
        contact= value

      if key== "email":
        email= value

      if key== "password":
        password= value


      flag2=0

      if re.search('[a-z]', contact):
        flag2=1

      if re.search('[A-Z]', contact):
        flag2=1

      if len(contact) < 10 or len(contact) > 10:
        flag2=1


      
    if flag2 == 1:
        messages.error(request, 'Enter a Valid Phone Number!')
         

    flag=0
    if not re.search('[a-z]', password):
      flag=1

    if not re.search('[0-9]', password):
      flag=1

    if not re.search('[A-Z]', password):
      flag=1

    if not re.search('[$@#%!]', password):
      flag=1

    if len(password) < 6:
      flag=1

    
    if(flag == 1):
      messages.error(request, 'The Password you entered is not valid!')
    


    if(flag == 0 and flag2 == 0):
      command= "insert into users values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(firstname, lastname, sex, city, state, contact, email, password)

      cursor.execute(command)
      obj.commit()

      messages.success(request, 'Your profile is registered successfully!')

    

    """template= render_to_string('email_template.html', {'name' : firstname})
    Sendmail= EmailMessage(
      'Thanks for registering on our website',
      template,
      settings.EMAIL_HOST_USER,
      [email],
    )

    Sendmail.fail_silently= False
    Sendmail.send()"""

  return render(request, 'signup_page.html')


