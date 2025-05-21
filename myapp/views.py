from django.shortcuts import render,redirect,HttpResponse
from .models import Postmodels
from .models import messagebox
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request): 
    posts =Postmodels.objects.all()
    return render(request,'home.html',{'posts':posts})

def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

       
        if password != confirm_password: 
            return redirect('signup')  

       
        if User.objects.filter(username=user_name).exists():
            
            return redirect('signup')

     
        if User.objects.filter(email=email).exists():
            
            return redirect('signup')

       
        my_user = User.objects.create_user(username=user_name, email=email, password=password)
        my_user.save()

        login(request, my_user)
        return redirect('homepage')
    
    return render(request,'signup.html')

def log_in(request):
        if request.method == 'POST':
            uname = request.POST.get('username')
            passlog = request.POST.get('password')
            user =authenticate(request,password=passlog, username=uname)
            if user:
                 login(request,user)
                 return redirect('homepage')
        return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect('login') 
 
@login_required(login_url='login')
def addpost(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        image = request.FILES.get('image') 
        post=  Postmodels(title=title,content=content,author=request.user,image=image)
        post.save()
        return redirect('homepage')
    return render(request,'add_post.html')

@login_required(login_url='login')
def message_view(request):
    if request.method == "POST":  
        message_content = request.POST.get('msg') 
        if message_content:  # Make sure the message is not empty
            msg = messagebox(message=message_content, author=request.user) 
            msg.save()
        return redirect('message')

    # Fetch all messages and order them by the datetime_sent field
    messages = messagebox.objects.all().order_by('-datetime_sent')  
    return render(request, 'message.html', {'messages': messages})







