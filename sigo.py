import sigo_api_helpers as si
import xml.etree.ElementTree as ET


def run_sigo():
    ip = si.get_ip()
    location_xml = ET.fromstring(si.get_location_xml(ip))

    latitude = location_xml.find("Latitude").text
    longitude = location_xml.find("Longitude").text

    weather_xml = ET.fromstring(si.get_weather_xml(latitude, longitude))

    score = 4
    responses = ['absolutely not', 'probably not', 'maybe', 'could do', 'yeah!']

    temperature = float(weather_xml.find("temperature").attrib.get("value"))

    if temperature > 40 or temperature < 12:
        score -= 1
    elif temperature < 5:
        score -= 3

    wind = float(weather_xml.find("wind").find("speed").attrib.get("value"))

    if wind > 20:
        score -= 1
    elif wind > 30:
        score -= 3

    clouds = float(weather_xml.find("clouds").attrib.get("value"))

    if clouds > 50:
        score -= 1
    elif clouds > 80:
        score -= 3

    rain = weather_xml.find("precipitation").attrib.get("mode")

    if rain != "no":
        score -= 3

    return responses[score]


def main():
    print run_sigo()

if __name__ == "__main__":
    main()