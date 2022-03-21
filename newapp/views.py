from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse

#importing loading from djano template
from django.template import loader
from newapp.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


from newapp.models import User

from newapp.models import addemployee1
from newapp.form import addemployee2

from newapp.models import addstudent1
from newapp.form import addstudent2



# login code
def logis(request):
    if request.method=='POST':
        usern=request.POST.get('email')
        print(usern)
        if usern=='leninpaul56@gmail.com':
            print('88888888888888888')
            return render(request,'adminpage.html')
        else:
            return HttpResponse('<h3>Invalid Details!! Please enter valid credintials</h3>')
    else:
        print('invalid')
        return render(request,'home.html')




# employee add & submit
def saveemployee(request):
    if request.method=='POST':
        form=addemployee2(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Employee Added Sucessfully.</h3>')
    else:
        form=addemployee2()
        return render(request,'addemployee.html',{'emp':form})


# employee view
def empview(request):
    emv=addemployee1.objects.all()
    return render(request,'empshow.html',{'empshow':emv})


# emp delete
def empdelete(request,id):
    empdel=addemployee1.objects.get(id=id)
    empdel.delete()
    return redirect('/viewemployee')


# emp edit
def editemployee(request,id):
    editemp=addemployee1.objects.get(id=id)
    return render(request,'empedit.html',{'editem':editemp})

# emp update
def updateemployee(request,id):
    editemp=addemployee1.objects.get(id=id)
    form11=addemployee2(request.POST,instance=editemp)
    if form11.is_valid():
        form11.save()
        return redirect('/viewemployee')
    return render(request,'empedit.html',{'editem':editemp})




# add student form
def addstudent3(request):
    if request.method=='POST':      
        usern=request.POST.get('st_name')
        regno=request.POST.get('st_regno')
        place=request.POST.get('st_place')
        dept=request.POST.get('st_dept')
        passw=request.POST.get('st_mob')
        n=addstudent1.objects.create(st_name=usern,st_regno=regno,st_place=place,st_dept=dept,st_mob=passw)
        n.save()
        request.session['studId']=n.id
        return redirect('/addmarkpage')
    else:
        return render(request,'stuadd.html')


# this page is redirection of add student page 
def addmark(request):
    markform=addstudent1.objects.filter(id=request.session['studId'])
    return render(request,'addmarks.html',{'markform':markform})


