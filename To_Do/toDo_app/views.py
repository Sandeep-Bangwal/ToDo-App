from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from . models import tasks

# Create your views here.

def home(request):
    dis = tasks.objects.filter(user_id =request.session['user'] )

    return render(request, "index.html" ,{'dis':dis})

def hendle_signUp(request):
    if request.method == 'POST':
     username = request.POST['username']
     Password = request.POST['Password']
     email = request.POST['email']
     Cpassword = request.POST['Cpassword']


    #  chek for error input
     if (Password != Cpassword):
       messages.error(request, "Password Do not match")
       return redirect('hendle_signUp')

     add_user = User.objects.create_user(username,email, Password)
    #  add_user.set_password(Password)
     add_user.save()
     messages.success(request, "Your account create successfully....")
     return redirect('hendle_login')

    else:
       return render (request, "signUp.html")

def hendle_login(request):
    if request.method == 'POST':
     username = request.POST['username']
     password = request.POST['Password']
     
     user=authenticate(username= username, password= password)
    

     if user is not None:
      login(request, user)
      request.session['user'] = user.id
      print(request.session['user'] )
      messages.success(request, "Successfully Logged In")

      return redirect("home")
     else:
      messages.error(request, "Invalid credentials! Please try again")
      return HttpResponseRedirect(request.path_info)
    else:
     return render(request, "login.html")   

def handel_Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('hendle_login') 

def addTasks(request):
   if request.method == 'POST':
     Tasks = request.POST['tasks']
     user_id = request.POST['user_id']
     add_tasks = tasks(tasks_desc=Tasks, user_id=user_id).save()
   return redirect("home")


def delete(request,id):
  del_tasks = tasks.objects.get(task_id = id).delete()
  messages.success(request, "Successfully deleted..")
  return redirect("home")

def Finished(request,id):
    finished_tasks = tasks.objects.get(task_id = id)
    finished_tasks.status = "Finished Tasks"
    finished_tasks.save()
    messages.success(request, "Your Tasks is finished..")
    return redirect("home") 