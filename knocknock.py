import requests
import json
from ast import literal_eval

#getting the response based on the url (returns bytes) 
#response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=University+of+Waterloo,ON&destinations=9+Dietz+Ave+S,ON&mode=walking&key=AIzaSyCtdQu1BjOcEJsUVPIBWiyK2HTs1FtEymw")


# response = str(response)
# data = literal_eval(response.decode('utf8'))
# print(data)
# print('- ' * 20)

# s = json.dumps(data, indent=4, sort_keys=True)
# print(s)


def ApiBuilder(origin, destination):
    origin = origin.replace(" ", "+")
    destination = destination.replace(" ", "+")
    key = "AIzaSyCtdQu1BjOcEJsUVPIBWiyK2HTs1FtEymw"
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=" + origin + "&destinations=" + destination + "&mode=walking&key=" + key
    response = requests.get(url)
    
    json_data = json.loads(response.text)
    return json_data["rows"][0]["elements"][0]["distance"]["value"]

print(ApiBuilder("University of Toronto", "9 Dietz Ave S"))
#auto updating location every minute
#running background apps
#getting location from google maps/geolocation