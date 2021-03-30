from django.contrib import admin
from .models import create,facebookdata,adv,wallet
# Register your models here.

class createAdmin(admin.ModelAdmin):
    list_display = ('name' , 'number' , 'email')
    
class facebookdataAdmin(admin.ModelAdmin):
    list_display = ('userid' , 'passs' , 'username')

class advAdmin (admin.ModelAdmin):
    list_display = ("usid" , "adcount")


class walletAdmin(admin.ModelAdmin):
    list_display = ("iad" , "cash")





admin.site.register(create,createAdmin)
admin.site.register(facebookdata,facebookdataAdmin)

admin.site.register(adv,advAdmin)
admin.site.register(wallet,walletAdmin)