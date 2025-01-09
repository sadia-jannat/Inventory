from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#add first create
from django.contrib import admin
from inentory_app import views
#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
#query ar jonno
from django.db.models import Q

#django signup and login
from django.contrib.auth.forms import UserCreationForm
from .forms import Create
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


from .models import *
from .forms import *




def Home(request):

    device=DeviceProuct.objects.all()

#likelihood start with bar
    Laptop1=DeviceProuct.objects.filter(device_number=65).count()
    Laptop2=DeviceProuct.objects.filter(device_number=20).count()
    Laptop3=DeviceProuct.objects.filter(device_number=45).count()
    Laptop4=DeviceProuct.objects.filter(device_number=78).count()
    
    x=[Laptop1,Laptop2,Laptop3,Laptop4]
    y=[65,20,45,78]

   
    context={
        'device':device,
        'x':x,
        'y':y,
         } 

    return render(request, "Home.html", context)              


def stuff_signup(request):
     form=Create()
    
     if request.method == "POST":
        form=Create(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account create successfully!!')
            
     context={'form':form}  
     return render(request,"stuff_signup.html",context)    


login_result=1
def stuff_login(request):
    
    if request.method == "POST":       
        username=request.POST.get('username')
        password=request.POST.get('password') 
        user=authenticate(request, username=username, password=password)

        if user is not None:
            global login_result
            login_result=0
            
            login(request,user)

            return redirect('/home/') #('/search/')

        else:
            messages.info(request,'Username and password incorrect')
    return render(request,"stuff_login.html")

def stuff_logout(request):
    logout(request)
    return redirect('/')     


#device add
def DeviceAddForm(request):

    if request.method =="POST":
        de=DeviceProuct()

        de.brand = request.POST.get('brand')
        de.modelname=request.POST.get('modelname')
        de.device_series = request.POST.get('device_series')
        de.device_number = request.POST.get('device_number')
        de.processor_brand= request.POST.get('processor_brand')
        de.generation=request.POST.get('generation')
        de.processor_model = request.POST.get('processor_model')
        de.cpu_cache= request.POST.get('cpu_cache')
        de.display_size= request.POST.get('display_size')
        de.display_type= request.POST.get('display_type')
        de.display_resolution= request.POST.get('display_resolution')
        de.touch_screen= request.POST.get('touch_screen')
        de.ram= request.POST.get('ram')
        de.ram_type= request.POST.get('ram_type')
        de.hdd= request.POST.get('hdd')
        de.ssd= request.POST.get('ssd')
        de.optical_drive= request.POST.get('optical_drive')
        de.keyboard_back_lit= request.POST.get('keyboard_back_lit')
        de.finger_print_sensor= request.POST.get('finger_print_sensor')
        de.wifi= request.POST.get('wifi')
        de.operating_system= request.POST.get('operating_system')
        de.weight= request.POST.get('weight')
        de.warranty= request.POST.get('warranty')

        de.save()

        messages.info(request,'Your data added successfully!!')
                    
    return render(request, "DeviceAdd.html")




#stuff dashborad
def Dashboard(request):
    formvar=DeviceProuct.objects.all() 
    return render(request, "UserDasboard.html", {'formvar':formvar})

def dashboard_delete(request,id):
    if request.method == 'POST':
        pi=DeviceProuct.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/userpage')    

def dashboard_edit(request, id):
    if request.method == 'POST':
         pi=DeviceProuct.objects.get(pk=id)
         fm=DeviceProuctForm(request.POST, instance=pi)
         if fm.is_valid():
             fm.save()  

    else:
           pi=DeviceProuct.objects.get(pk=id)
           fm=DeviceProuctForm(instance=pi)
    

   
    context={'fo':fm,
             'pi':pi}      
    return render(request, 'edit.html', {'fo':fm})  


def search(request):
    
    #start seach
    max_price = request.GET.get('max_price')
    min_price = request.GET.get('min_price')
     
    house_list = DeviceProuct.objects.filter(device_number__range=(min_price, max_price))
    #end
            
    #start 
    products=DeviceProuct.objects.all() 

    if request.method == 'GET':
        query = request.GET.get('query')
        queryx=request.GET.get('queryx')
        queryy=request.GET.get('queryy')
        

        if query:
            products = DeviceProuct.objects.filter(brand__icontains=query).order_by('brand') 
        elif queryx:
            products = DeviceProuct.objects.filter(device_number__icontains=queryx).order_by('brand') 
        elif queryy:
            products = DeviceProuct.objects.filter(device_number__range=(20,90)).order_by('brand')  
        else:
            print("No information to show")
    
    context={'house_list':house_list,'products':products}

    return render(request, 'search.html', context)  




def sale_add(request):

    if request.method =="POST":
        inven=InventoryLevel()

        inven.sales_summaries = request.POST.get('sales_summaries')
        inven.stuff=request.POST.get('stuff')
        inven.stock_type = request.POST.get('stock_type')
        inven.stock_range = request.POST.get('stock_range')
        inven.sales_num= request.POST.get('sales_num')
        inven.lastdate=request.POST.get('lastdate')

        inven.save()

        messages.info(request,'Your data added successfully!!')

    return render(request, "sale_add.html")    



def sale_details(request):

    sale=InventoryLevel.objects.all() 
    return render(request, "sale_details.html", {'sale':sale})





     


  

