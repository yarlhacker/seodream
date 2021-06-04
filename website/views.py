from django.shortcuts import render
from . import models 
from service import models as models_service 
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    config  = models.Configuration.objects.filter(status=True).first()
    website  = models.Website.objects.filter(status=True).first()
    statistiques = models.Stat.objects.filter(status=True)
    banner  = models.Banner.objects.filter(status=True).first()
    features = models_service.Feature.objects.filter(status=True)
    about = models.About.objects.filter(status=True).first()
    services = models_service.Service.objects.filter(status=True)
    portfolios = models_service.Portfolio.objects.filter(status=True)
    return render(request , 'index.html',locals())


@csrf_exempt 
def post_contact(request):
    success , msg = True , 'Votre message a bien été envoyer'
    users = json.loads(request.POST.get('users'))
    
    for user in users:
        if not user.get('name') or user.get('name').isspace() :
           success = False
           mgs = 'veuillez entre votre nom'
        elif not user.get('surname') or user.get('surname').isspace():
           sucsess = False
           mgs = 'veuillez entre votre surnom'
        elif not user.get('email') or user.get('email').isspace():
           success = False
           mgs = 'veuillez entre votre email'
        else:
            contacts = models_service.Contact()
            contacts.name = user.get('name')
            contacts.surname = user.get('surname')
            contacts.email = user.get('email')
            contacts.subject = user.get('subject')
            contacts.message = user.get('message')
            contacts.save()

    datas = {

        'success':success,
        'message': msg 
    }
    return JsonResponse(datas, safe= False)




# Create your views here.
