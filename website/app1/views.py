from django.shortcuts import render
from .models import chat, botrespond
from django import template
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import registraionform
from django.http import HttpResponse, JsonResponse
from django.template import loader


def index(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
               # students = Student.objects.filter(user=request.user)
                #message = Student_message.objects.filter(student=request.student)

                return render(request, 'chat.html', {'user': user, 'alluser':User.objects.all(),'currentuser':'' })
            else:
                return render(request, 'home.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home.html', {'error_message': 'Invalid login'})

    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmpassword']
        if str(password2) == str(password1):
            user = User.objects.create_user(username=username,
                                            first_name=firstname,
                                            last_name=lastname,
                                            email=email,
                                            password=password1)
            return render(request, 'home.html', {'error_message': 'Succesfully signed up'})
        else:
            return render(request, 'home.html', {'error_message': 'Password doesnot match'})

    return render(request,'home.html')

reciever = User.objects.get(pk=1)
sender =  User.objects.get(pk=1)
def msgbox(request,user_id):
    global reciever
    reciever = User.objects.get(pk=user_id)
    global sender
    sender = request.user
    msgs = chat.objects.all()
    return render(request,'msgbox.html',{'reciever':reciever, 'sender':sender,'msgs':msgs})

def post(request):

    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = chat(fromuser=request.user, touser=reciever, message=msg)
        if msg != '':
            c.save()
        if reciever.pk == 9:
            ans=botrespond.objects.get(question = msg)
            ans=ans.answere
            c = chat(fromuser=reciever, touser=request.user, message=ans)
            c.save()
        return JsonResponse({'msg':msg,'user':c.fromuser.username})
    else:
        return HttpResponse('Request must be POST.')


def Messages(request):
    c = chat.objects.all()
    return render(request, 'messages.html', {'chat': c, 'reciever':reciever, 'sender':sender})


