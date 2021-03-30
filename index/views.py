from django.shortcuts import render,redirect
from .models import create,facebookdata,adv
# Create your views here.



pop=False
#index pagge
pop2=False

def index(req):
    aa=""
    ads=""
    test=req.session.get('ui')
    if test:
         aa=adv.objects.filter(usid=test)
   
    if aa:
        print("yes")
        
    else:
        if test:
            adv(usid=test,adcount=0).save()
        
    if test :
        ads = adv.objects.get(usid=test).adcount
    
    
    if test:
        pop=True
        
    else:
        pop=False
    pop2test=facebookdata.objects.filter(userid=test)
    if pop2test:
        pop2=True
        
    else:
        pop2=False
        
    print(pop2)
    
    return render(req,'index.html',{'pp':pop,'poop2':pop2,"cop":ads})
    
    
    
    
#Create account


def creae(req):
    
    nm=req.POST['name']
    number=req.POST['number']
    email=req.POST['email']
    
    print(nm)
    print(email)
    print(number)
    
    create(name=nm,email=email,number=number).save()
    
    uid=create.objects.get(email=email).id
    
    req.session['ui']=uid
    
    return redirect('index')
    
    
    
    
def login(req):
    
    return render(req,'index.html')
    
    
    
    
#log out

def logout(req):
    req.session.clear()
    return redirect('index')
    





