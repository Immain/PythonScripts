# Get Geo-Location Info of User
import requests
import os
import json

# Get the current user
user = os.getlogin()

# Get the IP Address of the user
ip = requests.get('https://api.ipify.org').text

# Get the Geo-Location Info of the user
url = 'http://ip-api.com/json/'
response = requests.get(url+ip)
data = response.json()

# initialize JSON data
json_data = '{"user": "'+user+'", "ip": "'+ip+'", "city": "'+data['city']+'", "region": "'+data['regionName']+'", "country": "'+data['country']+'", "lat": "'+str(data['lat'])+'", "lon": "'+str(data['lon'])+'"}'

# Create Python Object from JSON data
python_obj = json.loads(json_data)

# Print the Geo-Location Info of the user
json_formatted_str = json.dumps(python_obj, indent=2)
print(json_formatted_str)
