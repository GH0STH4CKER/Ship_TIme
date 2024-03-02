from timezonefinder import TimezoneFinder
import datetime
import pytz,requests,json
from colorama import Fore

url = "https://api.searoutes.com/vessel/v2/9713351/position"

headers = {
    "accept": "application/json",
    "x-api-key": "fcodiFKiqp2bAXwNXxLDT3BgPePEKt743VkxM9UN"
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
        local_time = datetime.datetime.now(timezone)

        return local_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    else:
        return "Timezone not found for the given coordinates."

if lon and lat:
    latitude = lat
    longitude = lon

    local_time = get_local_time(latitude, longitude)
    print(Fore.GREEN+"Local Time:", local_time)

