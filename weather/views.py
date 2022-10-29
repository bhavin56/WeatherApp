from urllib import response
from django.shortcuts import render
import json
import urllib
import os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = str(os.environ.get('API_KEY'))
        req = urllib.request.Request('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+'')
        request1 = urllib.request.urlopen(req)
        json_data=json.load(request1)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),
            # "Sea_level" : str(json_data['main']['sea_level']),
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})