from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import Library

from .models import extenduser,complaindata
from django.contrib import auth

def index(request):
    return render(request,'myapp/index.html')

def register(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['mobile'])
            return redirect(register)
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['mobile'],password=request.POST['pw'])
            user.save()
            userdata = extenduser(firname=request.POST['name'],
            fname=request.POST['father'],
            gnpan=request.POST['gramp'],
            gramp=request.POST['gram'],user=user)
            userdata.save()
            return redirect(login)
    else:
        return render(request,'myapp/register.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['lmobile'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect(complain)
        else:
            return render(request,'myapp/login.html')
    else:
        return render(request,'myapp/login.html')


@login_required(login_url='/login/')
def complain(request):
    if request.method == 'POST':
            complain_data = complaindata(department = request.POST['depart1'],gram_nagar = request.POST['gpan'],
                                     com_subject = request.POST['comsub'],
                                     description = request.POST['descr'],
                                     upload_file = request.FILES['myfile'],
                                     user = request.user)
            complain_data.save()
            msg="Compalin Done Succcessfully!!!"
            extenddata = extenduser.objects.filter(user=request.user)
            complaindata1 = complaindata.objects.filter(user=request.user)
            return render(request, 'myapp/complain.html',{'extenddata':extenddata,'complaindata1':complaindata1,'msg':msg})
    else:
        extenddata= extenduser.objects.filter(user = request.user)
        return render(request, 'myapp/complain.html',{'extenddata':extenddata})


def adminview(request):
    data = complaindata.objects.all()
    return render(request,'myapp/admin.html',{'data':data})



def admin(request):

    if request.method == 'POST':
        pw = request.POST['password']
        user=auth.authenticate(username='MLA',password=pw)
        if user is not None:
            auth.login(request,user)
            return render(request, 'myapp/admin.html')
        else:
            return render(request,'myapp/index.html')
    else:
        return render(request, 'myapp/index.html')


def logout(request):
    auth.logout(request)
    return redirect(index)

def viewcomplain(request):
        extenddata = extenduser.objects.filter(user = request.user)
        complaindata1=complaindata.objects.filter(user=request.user)
        return render(request,'myapp/viewcomplain.html',{'extenddata':extenddata,'complaindata1':complaindata1})


def changestatus(request,id):
    obj=complaindata.objects.get(id=id)
    if request.method=='POST':
        obj.status=request.POST['updateStatus']
        obj.save()
        return render(request, 'myapp/admin.html')
    else:
        return render(request,'myapp/changestatus.html',{'obj':obj})
