
from urllib.request import Request, urlopen
import json
import time
def get_incidents(lat, long, radius):
    incidents = []
    url = "https://citizen.com/api/incident/trending?lowerLatitude=" + str(lat-radius) + "&lowerLongitude=" + str(long-radius) + "&upperLatitude=" + str(lat+radius) + "&upperLongitude=" + str(long+radius)+ "&fullResponse=true&limit=20"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    data = json.loads(webpage.read().decode(webpage.info().get_param('charset') or 'utf-8'))
    for i in data["results"]:
        text = i["raw"]
        print(text)
        timestamp = i["ts"]
        rawloc = i["rawLocation"]
        lat = i["latitude"]
        long = i["longitude"]
        severity = i["severity"]
        key = i["key"]
        police = i["police"]
        timestamp = time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(timestamp/1000))
        print(timestamp)
        incidents.append([text, timestamp, rawloc, lat, long, severity, key, police])
    return(incidents)

 
