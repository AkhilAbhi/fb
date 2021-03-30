from django.shortcuts import render,redirect
from .models import create,facebookdata,adv,wallet


def index(req):
    
    ad2="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-yFUOuJr_sAlytTwBLTUVNxMGcHWa_jSlkw&usqp=CAU"
    
    
    ad3="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNV07cKTOZUGXpv-7wfVG6GgLF-L2fNp0rwQ&usqp=CAU"
    
    
    ad4="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyvOMBTyYigk-RdLogHu7N3IApTYepskLLGA&usqp=CAU"
    
    ad5="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSf2ulwDgk8BVEOQFU0JOubDxly7KiUxOWrSA&usqp=CAU"
    mm=req.session.get("ui")
    cc=adv.objects.get(usid=mm).adcount
   
    p=req.GET.get("t")
    if p == "task1":
        print(cc)
        if cc == "0":
            print("hello")
            return render(req,"click.html",{"nm":p})
        else:
            return redirect('index')
        
    elif p == "task2":
        if cc == "1":
            return render(req,"chek.html",{"img":ad2,"nm":p})
            
        else:
            return redirect("index")
        
        
    elif p == "task3":
        
        if cc == "2":
            return render(req,"chek.html",{"img":ad3,"nm":p})
        else:
            return redirect("index")
        
        
    elif p == "task4":
        if cc == "3":
            return render(req,"chek.html",{"img":ad4,"nm":p})
        else:
            return redirect('index')
        
    elif p == "task5":
        if cc == "4":
            return render(req,"chek.html",{"img":ad5,"nm":p})
        else:
            return redirect('index')
        
    
    


def complet(req):
    views =  0
    dataa=req.GET["tname"]
    iid = req.session.get("ui")
    print(iid)
    ca=0
    
    mp=wallet.objects.filter(iad=iid)
   
    if dataa == "task1":
        if mp :
            cas=1
            
        else:
            cas=1
            wallet(iad=iid,cash=cas).save()
        
        views=1
    elif dataa == "task2":
        cas=3
        views=2
    elif dataa == "task3":
        cas=5
       
        views=3
    elif dataa == "task4":
        cas=7
    
        views=4
    elif dataa == "task5":
        cas=10
        views=5
    
    
    tp=adv.objects.filter(usid=iid)
    tp.update(adcount=views)
    ma=wallet.objects.filter(iad=iid)
    ma.update(cash=cas)
    return redirect("index")
        