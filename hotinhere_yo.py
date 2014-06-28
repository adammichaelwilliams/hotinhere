import requests
import json

api_key_file = open('api.key', 'r')

api_token =  api_key_file.read().split('\n')[0]

fct_url = 'http://api.wunderground.com/api/ea5c64c3975ff6cd/hourly/q/CA/San_Francisco.json'
cond_url = 'http://api.wunderground.com/api/ea5c64c3975ff6cd/conditions/q/CA/San_Francisco.json'

fct_req = requests.get(fct_url)
cond_req = requests.get(cond_url)

fct_json = json.loads(fct_req.text)
cond_json = json.loads(cond_req.text)

fct_temp = fct_json['hourly_forecast'][0]['temp']['english']
cond_temp = cond_json['current_observation']['temp_f']

fct_temp = float(fct_temp)

print "Forecasted temp: " + str(fct_temp)
print "Current temp: " + str(cond_temp)

if(cond_temp > fct_temp and cond_temp > 70):
    print "Send Yo!"
    requests.post("http://api.justyo.co/yoall/", data={'api_token': api_token})    

