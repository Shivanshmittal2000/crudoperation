from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.conf.urls.static import static

# Create your views here.
def index(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            users=User.objects.all()
            print(users)
            fm=StudentRegistration()
    else :
        fm=StudentRegistration()
        users=User.objects.all()
    return render(request,'enroll/addnew.html',{'form':fm,'users':users})