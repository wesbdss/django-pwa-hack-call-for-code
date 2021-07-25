from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from django.utils import timezone
import time
import datetime
from .models import Cultivo, Foresta

# time_request =timezone.now()-datetime.timedelta(days=1)
# response = {}
# def get_cotacao():
#     global time_request
#     global response
#     if timezone.now() > (time_request+datetime.timedelta(days=1)) and response.get('value'):
#         driver = None
#         options = Options()
#         options.headless = False
#         driver = webdriver.Firefox(options=options,executable_path=GeckoDriverManager().install())
#         driver.get('https://br.investing.com/commodities/carbon-emissions-streaming-chart')
#         time.sleep(2)
#         value = driver.find_element_by_id("last_last").text
#         variancia = driver.find_element_by_class_name('pid-8848-pc').text
#         types = [x.text for x in driver.find_elements_by_class_name("elp")]
#         response = {
#             "value":value,
#             "variancia":variancia,
#             "unidade":types[2],
#         }
#         time_request = timezone.now()
#     return response 

    
# Create your views here.
def offline(request):
    return render(request,'offline.html')

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('root:homepage'))
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            authlogin(request,user)
            return HttpResponseRedirect(reverse('root:homepage'))
    return render(request, 'login/index.html')

@login_required(login_url='/login/')
def homepage(request):
    content = {
        "value":50.95,
        "variancia":0.16,
        "unidade":'tonelada',
        }

    kg_mes = None
    try:
        print(request.GET.get("cultivo"),request.GET.get("floresta"),request.GET.get("hectares"))
        if int(request.GET.get("cultivo")) and int(request.GET.get("hectares")):
            cultivo = Cultivo.objects.get(pk=request.GET.get("cultivo"))
            # quilo hectar mes
            kg_mes = cultivo.kgco2*float(request.GET.get("hectares"))
    except Exception as ex:
        pass
    try:
        if int(request.GET.get("floresta")) and int(request.GET.get("hectares")):
            floresta = Foresta.objects.get(pk=request.GET.get("floresta"))
            kg_mes = floresta.kgco2*float(request.GET.get("hectares"))
    except Exception as ex:
        pass
  



    # try:
    #     content=get_cotacao()
    # except Exception as ex:
    #     print(">>>>",ex)
    #     response = {}
    #     content = {
    #     "value":0,
    #     "variancia":0,
    #     "unidade":'tonelada',
    #     }
    content["floresta"]=Foresta.objects.all()
    content["cultivo"]=Cultivo.objects.all()
    if kg_mes:
        content['result'] = {
            "tonelada":"%.2f" % (kg_mes/1000),
            "valormes":"%.2f" % ((kg_mes/1000)*content.get("value"))
        }
    return render(request,'profile/index.html',{"content": content})

@login_required(login_url='/login/')
def logout(request):
    authlogout(request)
    return HttpResponseRedirect(reverse('root:login'))


