from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import StudentRegistration
from .models import User




# Create your views here.


#this function will add new item and show items
def add_show(request):

    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            un=fm.cleaned_data['userName']
            em=fm.cleaned_data['email']
            ph= fm.cleaned_data['phoneNumber']
            pw=fm.cleaned_data['password']
            cmnt=fm.cleaned_data['comment']
            
            reg=User(name=nm,userName=un,email=em,phoneNumber=ph,password=pw,comment=cmnt)
            reg.save()
            return HttpResponse('<h1>User Added Successfully</h1>')
    else:
        fm=StudentRegistration()
    stud= User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#this function will update/edit

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponse('<h1>User Updated Successfully</h1>')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration( instance=pi)
    return render (request,'enroll/updatestud.html',{'form':fm})

#this function will delete

def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponse('<h1>User deleted successfully</h1>')
