from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Blog
user_val = get_user_model()

@login_required
def delete_blog(request, blog_id):
    print(blog_id)

    blog = get_object_or_404(Blog, id=blog_id)
    print(blog)
    # Ensure the logged-in user is the owner of the blog or a superuser
    if blog.user == request.user :#request.user.is_superuser
        print('if')
        blog.delete()
        return redirect('home')  # Redirect to the list of blogs after deletion
    else:
        print('else')
        return redirect('home')  # You can also raise a permission

def add_blog(request):
    if request.method == 'POST':
        # Retrieve the data from the request
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('imageUpload')
        print(title,description,image)
        # Create a new blog entry
        if title and description and image:
            blog = Blog(title=title, description=description, image=image,user=user_val.objects.get(pk=request.user.pk))
            blog.save()
            return redirect('home')  # Redirect to the blog list after saving
        else:
            return HttpResponse("Missing data", status=400)  # Handle missing data

    return render(request, 'addblog.html')

def update(request):
    if request.method == "POST":
        # Assuming you're receiving data in JSON format
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        name = request.POST.get('username')
        email = request.POST.get('email')
        user = request.user

        # Update the fields
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.username = name

        # Save the changes
        user.save()
        messages.info(request, "saved")
        return redirect('update')
    else:
        return redirect('home')
def logout(request):
    auth.logout(request)
    return render(request, 'login3.html')
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            blogs = Blog.objects.filter(user=request.user )
            return render(request, 'home.html', {'blogs': blogs})
        else:
            messages.info(request, "Invalid credintials")
            return render(request, 'login3.html')
    else:
         return render(request,'login3.html')
def signup(request):
    if request.method=='POST':
        #Register code
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        if User.objects.filter(username=name).exists():
            messages.info(request,'Existing user')
            return render(request, 'signup.html')
        elif password != confirm_password:
            messages.info(request, 'Confirm password not matching')
            return render(request, 'signup.html')
        elif name and password:
            user = User.objects.create_user(username=name,password=password,first_name=firstname,last_name=lastname,email=email)
            user.save()
            return render(request, 'login3.html')
        else:
            messages.info(request, 'Retry error occured')
            return render(request, 'signup.html')

    return render(request,'signup.html')
def forgotpass(request):
    return render(request,'forgotpass.html')
def home(request):
    try:
        blogs = Blog.objects.filter(user=request.user)
        return render(request, 'home.html', {'blogs': blogs})
    except:
        return render(request, 'home.html')


def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def profile(request):
    user = request.user

    # You can access various properties of the user, like:
    username = user.username
    email = user.email
    firstname=user.first_name
    lastname=user.last_name
    is_authenticated = user.is_authenticated  # Checks if the user is authenticated

    # Pass user details to the template
    context = {
        'username': username,
        'email': email,
        'is_authenticated': is_authenticated,
        'firstname':firstname,
        'lastname':lastname
    }

    return render(request,'users_profile.html',context)
def addblog(request):
    return render(request,'addblog.html')

