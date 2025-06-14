def summarize_launch_status(weather):
    weather_main = weather["weather"][0]["main"]
    wind_speed = weather["wind"]["speed"]
    conditions = ["Thunderstorm", "Rain", "Snow", "Extreme"]  # Unsafe

    if weather_main in conditions or wind_speed > 15:
        return f"Launch may be delayed due to {weather_main.lower()} and wind speed of {wind_speed} m/s."
    return "Launch weather conditions appear to be normal."
