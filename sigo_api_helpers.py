import requests


def get_ip():
    """Return current IP address"""
    return requests.get("http://bot.whatismyipaddress.com").text


def get_location_xml(ip):

    return requests.get("http://freegeoip.net/xml/" + ip).text


def get_weather_xml(latitude, longitude):

    return requests.get("http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&mode=xml&units=metric".format(
        latitude, longitude)).text

