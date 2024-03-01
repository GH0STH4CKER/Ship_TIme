# Ship Time Documentation

This Python script utilizes the `timezonefinder` library to determine the timezone based on the latitude and longitude of a given ship's position. It then fetches the current local time at that location using the `datetime` and `pytz` libraries.

## Code Overview

### Libraries Used:
- `timezonefinder`: Used to find the timezone based on coordinates.
- `datetime`: Used to handle date and time.
- `pytz`: Used to handle timezones.
- `requests`, `json`: Used for making HTTP requests and handling JSON responses.

### Setup:
- `imo`: The International Maritime Organization (IMO) number of the ship.
- `your_api_key`: API key obtained from searoutes.com.
- `url`: URL for fetching ship position data is constructed based on the IMO number.

### Making API Request:
- Sends a GET request to the searoutes API to retrieve the ship's position data.

### Extracting Latitude and Longitude:
- Latitude and longitude coordinates are extracted from the response JSON.

### Function to Get Local Time:
- The `get_local_time` function takes latitude and longitude as input.
- It uses `timezonefinder` to determine the timezone at the given coordinates.
- Then, it gets the current time in that timezone and formats it.

### Fetching and Printing Local Time:
- If latitude and longitude are available, the local time at that location is fetched using the `get_local_time` function.
- The local time is printed in the format: "YYYY-MM-DD HH:MM:SS TimeZone".

## Usage
To use this script:
1. Replace `imo` with the IMO number of the ship.
2. Replace `your_api_key` with the API key obtained from searoutes.com.
3. Run the script.

### Accuracy
Calculated Time May have a difference of +1 or -1 hour
