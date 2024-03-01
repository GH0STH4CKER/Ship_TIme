from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz,requests,json

imo = "" #add imo no of the ship you want
your_api_key = "" # signup and obtain api key from searoutes.com

url = "https://api.searoutes.com/vessel/v2/"+imo+"/position"

headers = {
    "accept": "application/json",
    "x-api-key": "your_api_key"
}

response = requests.get(url, headers=headers)

data = json.loads(response.text)

lon,lat = data[0]['position']['geometry']['coordinates']


def get_local_time(latitude, longitude):
    # Initialize TimezoneFinder object
    tf = TimezoneFinder()

    # Get timezone for given latitude and longitude
    timezone_str = tf.timezone_at(lng=longitude, lat=latitude)

    if timezone_str:
        # Get timezone object
        timezone = pytz.timezone(timezone_str)

        # Get current time in the given timezone
        local_time = datetime.now(timezone)

        return local_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    else:
        return "Timezone not found for the given coordinates."

if lon and lat:
    latitude = lat
    longitude = lon

    local_time = get_local_time(latitude, longitude)
    print("Local Time:", local_time)
