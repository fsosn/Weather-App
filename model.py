import requests
import endpoints


class Model:
    def __init__(self, api_key):
        self.api_key = api_key
        self.weather_data = {}

    def get_location_key(self, city_name):
        url = (
            endpoints.base_url
            + "/"
            + endpoints.autocomplete_endpoint.format(self.api_key, city_name)
        )
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 and data:
                return data[0]["Key"]
            else:
                raise Exception("No location key found.")
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def fetch_weather_conditions(self, city, forecast_type):
        location_key = self.get_location_key(city)
        if location_key:
            endpoint = forecast_type + "_endpoint"
            url = f"{endpoints.base_url}/{getattr(endpoints, endpoint)}".format(
                location_key, self.api_key
            )
            try:
                response = requests.get(url)
                data = response.json()
                if response.status_code == 200 and data:
                    self.weather_data = data
                else:
                    raise Exception("Weather data is unavailable.")
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)

    def get_weather_data(self):
        return self.weather_data
