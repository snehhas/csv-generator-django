from django.shortcuts import *
from django.contrib.auth.forms import *
from .forms import *
from .models import *
from .tasks import *

# Create your views here.
# def home(request):
#     return render(request,'celeryapp/index.html',{"form":CustomForm()})

def success(request):
    return render(request,'celeryapp/success.html')

def finaldata(request):
    details = Details.objects.all()
    return render(request,'celeryapp/mydata.html',{'data':details})

def newfile(request):
    print("here --> {}".format(request))
    if request.POST:
        form = CustomForm(request.POST)
        if form.is_valid():
            filename = form.cleaned_data['filename']
            count = form.cleaned_data['count']
            generate_file(filename,count)
            instance = Details(filename= filename, count = count)
            instance.save()
            return render(request , 'celeryapp/success.html')
    return render(request,'celeryapp/home.html',{"form":CustomForm()})


