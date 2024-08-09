from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.

def home(request): #everytime a page is visited request is sent to backend here which is passed to view
    records = Record.objects.all() #grabs all records



    # Check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records}) #home page is returned from request


#def login_user(request):
#    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid(): #django func
            form.save()
            #auth and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form}) #pass form into webpage

    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        customer_record = Record.objects.get(id=pk) #instead of .all we are getting a single record with .get
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete() #django handles
        messages.success(request, "Record Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To do That")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added!")
                return redirect('home')
        #if they are not filling out the form they want to see the form
        return render(request, 'add_record.html', {'form':form}) #pass form into webpage
    else:
        messages.success(request, "You Must Be Logged In To do That")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record) #populate addrecord form with current_record
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Has Been Updated")
                return redirect('home')
        return render(request, 'update_record.html', {'form':form})     
    else:
        messages.success(request, "You Must Be Logged In To do That")
        return redirect('home')
