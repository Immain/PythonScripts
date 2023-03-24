#     ____                  __         ____        __           _____            __
#    / __ \____ _____  ____/ /___ _   / __ \____ _/ /_____ _   / ___/__  _______/ /____  ____ ___  _____
#   / /_/ / __ `/ __ \/ __  / __ `/  / / / / __ `/ __/ __ `/   \__ \/ / / / ___/ __/ _ \/ __ `__ \/ ___/
#  / ____/ /_/ / / / / /_/ / /_/ /  / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ (__  ) /_/  __/ / / / / (__  )
# /_/    \__,_/_/ /_/\__,_/\__,_/  /_____/\__,_/\__/\__,_/   /____/\__, /____/\__/\___/_/ /_/ /_/____/
#                                                                 /____/
# Written By: Immain
# Date Created: 3/23/2023
# Version: 1.0.0
# Title : Geo-Location Info
# Description: Get the Geo-Location Info  of the system user

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
