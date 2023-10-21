from model import Model
import forecast_options
from datetime import datetime


class ViewModel:
    def __init__(self, api_key):
        self.model = Model(api_key)

    def fetch_weather_conditions(self, city, forecast_option):
        self.model.fetch_weather_conditions(city, forecast_option)
        data = self.model.get_weather_data()
        return self.format_weather_data(data, city, forecast_option)

    def format_weather_data(self, data, city, forecast_option):
        if data:
            if forecast_option == forecast_options.CURRENT_CONDITIONS:
                return (
                    f"Current weather conditions for {city}:\n\n"
                    f"Temperature: {data[0]['Temperature']['Metric']['Value']}°C\n"
                    f"Real Feel: {data[0]['RealFeelTemperature']['Metric']['Value']}°C\n"
                    f"Condition: {data[0]['WeatherText']}\n"
                    f"Wind: {data[0]['Wind']['Speed']['Metric']['Value']} km/h, {data[0]['Wind']['Direction']['Localized']}\n"
                )
            elif forecast_option == forecast_options.HOURLY_FORECAST:
                info = f"Weather forecast for the next 12 hours for {city}:\n\n"
                for hourly_forecast in data:
                    info += (
                        f"Time: {datetime.fromisoformat(hourly_forecast['DateTime'][:-6]).strftime('%H:%M')}\n"
                        f"Temperature: {hourly_forecast['Temperature']['Value']}°C\n"
                        f"Condition: {hourly_forecast['IconPhrase']}\n"
                        f"Wind: {hourly_forecast['Wind']['Speed']['Value']} km/h, {hourly_forecast['Wind']['Direction']['Localized']}\n"
                        f"Rain Probability: {hourly_forecast['RainProbability']}%\n\n"
                    )
                return info
            elif forecast_option == forecast_options.ONE_DAY_FORECAST:
                return (
                    f"Weather forecast for tomorrow for {city}:\n\n"
                    f"Minimum Temperature: {data['DailyForecasts'][0]['Temperature']['Minimum']['Value']}°C\n"
                    f"Maximum Temperature: {data['DailyForecasts'][0]['Temperature']['Maximum']['Value']}°C\n"
                    f"Day: {data['DailyForecasts'][0]['Day']['IconPhrase']}\n"
                    f"Night: {data['DailyForecasts'][0]['Night']['IconPhrase']}"
                )
            elif forecast_option == forecast_options.FIVE_DAY_FORECAST:
                info = f"Weather forecast for the next 5 days for {city}:\n\n"
                for day_forecast in data["DailyForecasts"]:
                    info += (
                        f"Day: {datetime.strptime(day_forecast['Date'][:10], '%Y-%m-%d').strftime('%A')}\n"
                        f"Minimum Temperature: {day_forecast['Temperature']['Minimum']['Value']}°C\n"
                        f"Maximum Temperature: {day_forecast['Temperature']['Maximum']['Value']}°C\n"
                        f"Day: {day_forecast['Day']['IconPhrase']}\n"
                        f"Night: {day_forecast['Night']['IconPhrase']}\n\n"
                    )
                return info
            else:
                raise ValueError("Invalid forecast option.")
