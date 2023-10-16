import requests
from tkinter import messagebox
from endpoints import *
from datetime import datetime

def get_location_key(api_key, city_name, language):
    url = base_url + "/" + autocomplete_endpoint.format(api_key, city_name, language)
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200 and data:
            return data[0]["Key"]
        else:
            messagebox.showerror("Error", "Unable to retrieve location key for this city.")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return None

def fetch_current_conditions(api_key, city_entry, weather_display, language):
    city = city_entry.get()  
    location_key = get_location_key(api_key, city, language)
    
    if location_key:
        url = base_url + '/' + current_conditions_endpoint.format(location_key, api_key, language)
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 and data:
                weather_info = f"Current weather information for {city}:\n\n"
                weather_info += f"Temperature: {data[0]['Temperature']['Metric']['Value']}°C\n"
                weather_info += f"Real Feel: {data[0]['RealFeelTemperature']['Metric']['Value']}°C\n"
                weather_info += f"Condition: {data[0]['WeatherText']}\n"
                weather_info += f"Wind: {data[0]['Wind']['Speed']['Metric']['Value']} km/h, {data[0]['Wind']['Direction']['Localized']}\n"
                weather_display.config(text=weather_info)
            else:
                messagebox.showerror("Error", "Unable to retrieve current weather conditions.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def fetch_twelve_hour_forecast(api_key, city_entry, weather_display, language):
    city = city_entry.get()    
    location_key = get_location_key(api_key, city, language)
    
    if location_key:
        url = base_url + '/' + hourly_forecasts_endpoint.format(location_key, api_key, language)
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 and data:
                weather_info = f"Weather forecast for the next 12 hours for {city}:\n\n"
                for hourly_forecast in data:
                    weather_info += f"Time: {datetime.fromisoformat(hourly_forecast['DateTime'][:-6]).strftime('%H:%M')}\n"
                    weather_info += f"Temperature: {hourly_forecast['Temperature']['Value']}°C\n"
                    weather_info += f"Real Feel: {hourly_forecast['RealFeelTemperature']['Value']}°C\n"
                    weather_info += f"Condition: {hourly_forecast['IconPhrase']}\n"
                    weather_info += f"Wind: {hourly_forecast['Wind']['Speed']['Value']} km/h, {hourly_forecast['Wind']['Direction']['Localized']}\n"
                    weather_info += f"Rain Probability: {hourly_forecast['RainProbability']}%\n\n"
                weather_display.config(text=weather_info)
            else:
                messagebox.showerror("Error", "Unable to retrieve hourly weather forecast.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def fetch_tomorrows_forecast(api_key, city_entry, weather_display, language):
    city = city_entry.get()  
    location_key = get_location_key(api_key, city, language)
    
    if location_key:
        url = base_url + '/' + one_day_forecast_endpoint.format(location_key, api_key, language)
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 and data:
                weather_info = f"Weather forecast for tomorrow for {city}:\n\n"
                weather_info += f"Minimum Temperature: {data['DailyForecasts'][0]['Temperature']['Minimum']['Value']}°C\n"
                weather_info += f"Maximum Temperature: {data['DailyForecasts'][0]['Temperature']['Maximum']['Value']}°C\n"
                weather_info += f"Day: {data['DailyForecasts'][0]['Day']['IconPhrase']}\n"
                weather_info += f"Night: {data['DailyForecasts'][0]['Night']['IconPhrase']}"
                weather_display.config(text=weather_info)
            else:
                messagebox.showerror("Error", "Unable to retrieve tommorow's weather forecast.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def fetch_five_day_forecast(api_key, city_entry, weather_display, language):
    city = city_entry.get()
    location_key = get_location_key(api_key, city, language)
    
    if location_key:
        url = base_url + '/' + five_day_forecast_endpoint.format(location_key, api_key, language)
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 and data:
                weather_info = f"Weather forecast for the next 5 days for {city}:\n\n"
                for day_forecast in data['DailyForecasts']:
                    weather_info += f"Day: {datetime.strptime(day_forecast['Date'][:10], '%Y-%m-%d').strftime('%A')}\n"
                    weather_info += f"Minimum Temperature: {day_forecast['Temperature']['Minimum']['Value']}°C\n"
                    weather_info += f"Maximum Temperature: {day_forecast['Temperature']['Maximum']['Value']}°C\n"
                    weather_info += f"Day: {day_forecast['Day']['IconPhrase']}\n"
                    weather_info += f"Night: {day_forecast['Night']['IconPhrase']}\n\n"
                weather_display.config(text=weather_info)
            else:
                messagebox.showerror("Error", "Unable to retrieve five day weather forecast.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")