# Weather-App
## Overview 
Weather app is a desktop application built with PyQt5 and Python and is integrated with the AccuWeather API. <br>It allows users to retrieve city-specific weather information, such as current conditions, tomorrow's forecast as well <br>as 12-hour and 5-day forecast. The project is built using the MVVM (Model-View-ViewModel) architecture.

## Getting started
1. Clone the repository:
   ```
   git clone https://github.com/fsosn/Weather-App
   ```
2. Install required libraries:
   ```
   pip install -r requirements.txt
   ```
## Running the app
To run the app, execute the following command:
   ```
   python main.py api_key
   ```
`api_key` - an API key generated at https://developer.accuweather.com/
## How to use
1. Enter the name of the city and choose one of the suggestions from the list
2. Select one of the forecast options by clicking on the corresponding button
3. The weather data will be displayed in the weather display area.
