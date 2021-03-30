from django.shortcuts import render

# Create your views here.


def index(req):
    
    name=req.POST['name']
    number=req.POST['number']
    email=req.POST['email']
    
    print(name)
    print(email)
    print(number)
    return render(req,'index.html')