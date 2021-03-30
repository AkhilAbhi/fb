from django.shortcuts import render,redirect
from .models import create,facebookdata,wallet
# Create your views here.


def index(req):
    iid= req.session.get("ui")
    mm=wallet.objects.get(iad=iid).cash
    return render(req,'wallet.html',{"cs":mm})