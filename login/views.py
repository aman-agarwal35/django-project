from django.shortcuts import render
import mysql.connector as sql
from django.contrib import messages
import re

email= ''
password= ''
# Create your views here.

def loginaction(request):
  global email, password

  if request.method == "POST":
    obj= sql.connect(host= "localhost", user= "root", password= "anisha5409", database= "login")
    cursor= obj.cursor()
    data= request.POST

    for key,value in data.items():
      if key == "email":
        email= value

      if key == "password":
        password= value


    command= "select * from users where email = '{}' and password = '{}'".format(email, password)
    cursor.execute(command)
    t= tuple(cursor.fetchall())

    if t == ():
      messages.error(request, 'Incorrect Email ID or Password!')
    else:
      return render(request, 'welcome.html')

  
  return render(request, 'login_page.html')




      
    

    
  