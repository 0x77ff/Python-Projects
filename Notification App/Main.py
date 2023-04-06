import json
import requests
from plyer import notification
from dotenv import load_dotenv
import os
load_dotenv()

city = 'your city'
api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': os.getenv('APIKEY')})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

data = json.loads(response.text)

print(str(data['temp']))
    
notification.notify(  
    title = "My Weather",  
    message = "Tempurature is "+str(data['temp'])+"℃ in "+city,  
    #app_icon = 'icon.ico',  
    timeout = 10,  
    toast = True  
)  