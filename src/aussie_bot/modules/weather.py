"""find the weather per user name"""
import requests

ROOT_URL = "http://www.bom.gov.au/fwo/"
WEATHER_TEXT = (
    "{name} -- Location {username}'s Place --Time {local_date_time} -- The "
    "Wind is from the {wind_dir} -- Wind speed {wind_spd_kt} KPH -- Wind "
    "gusts {gust_kmh} KPH -- Air temps is {air_temp}{degree}C -- {temp_f}"
    "{degree}F -- Relative Humidity is {rel_hum}% -- Air Pressure is "
    "{press}kPa -- Rain {rain_trace} -- co-ord's Lon/Lat {lon}/{lat}"
)
FIELDS = {
    "rain_trace",
    "degree",
    "temp_f",
    "rel_hum",
    "local_date_time",
    "press",
    "wind_dir",
    "air_temp",
    "name",
    "gust_kmh",
    "wind_spd_kt",
    "username",
    "lat",
    "lon",
    "sea_state",
}
USER_LOOKUP = {
    "sveta": "IDN60901/IDN60901.94767.json",
    "oksana": "IDN60901/IDN60901.94767.json",
    "berg": "IDN60801/IDN60801.94785.json",
    "bluemaxima": "IDN60801/IDN60801.94733.json",
    "dodobrain": "IDQ60901/IDQ60901.94575.json",
    "thearm": "IDN60801/IDN60801.94592.json",
    "ukn0me": "IDW60801/IDW60801.95610.json",
    "dooblynoobly": "IDQ60901/IDQ60901.94576.json",
    "doobz": "IDQ60901/IDQ60901.94576.json",
    "oobz": "IDQ60901/IDQ60901.94576.json",
    "sydneyi": "IDN60901/IDN60901.94768.json",
    "duoi": "IDN60801/IDN60801.95704.json",
    "mwsb": "IDN60801/IDN60801.94926.json",
    "dudz": "IDN60801/IDN60801.95757.json",
    "chris": "IDN60901/IDN60901.94768.json",
    "macspud": "IDV60901/IDV60901.95936.json",
    "mcspud": "IDV60901/IDV60901.95936.json",
    "veritay": "IDV60901/IDV60901.95936.json",
    "wyoung": "IDN60801/IDN60801.94749.json",
    "win32user": "IDN60901/IDN60901.94765.json",
    "orlock": "IDV60801/IDV60801.94864.json",
    "pebbles": "IDV60901/IDV60901.94872.json",
    "bluemaxima": "/IDN60901/IDN60901.94781.json",
}
def _parse_response(response):
    description = response.get('weather')
    try:
        d = description[0]
    except IndexError:
        main = desc = None
    else:
        main, desc = d['main'], d['description']

    lat = response.get('coord', {}).get('lat')
    lon = response.get('coord', {}).get('lon')



    return {
        'main': main,
        'temp': response.get('main', {}).get('temp', 0),
        'name': response.get('name'),
        'country': response.get('sys', {}).get('country'),
        'description': desc.capitalize(),
        'wind_speed': response.get('wind', {}).get('speed'),
        'humidity': response.get('main', {}).get('humidity'),
        'pressure': response.get('main', {}).get('pressure'),
        'visibility': response.get('sys', {}).get('visibility', 'clear'),
        'lat': lat,
        'lon': lon
        }


def _stiv_bullshit():
    """define stiv's weather"""
    url = "https://api.weather.gov/stations/KIGQ/observations/current"
    return url


def _get(weather_data, item):
    """get the data from url"""
    return weather_data.get(item, "")


def _format_output(**values):
    """set the format up for the output"""
    return WEATHER_TEXT.format(**values)


def _calculate_temp_in_c(temp):
    """return the calculated celcius  to farenheit"""
    return str((temp * 9 / 5.0 + 32) if temp else "")

def disavowed_bullshit(url):
    

    resp = requests.get(url).json()
    print (_parse_response(resp))
    lon = (str(resp['coord']['lon']))
    lat = (str(resp['coord']['lat']))
    for item in (resp['weather']):
        sky =(item['description'])
    temp = (resp['main']['temp'])
    pressure = (resp['main']['pressure'])
    humidity = (resp['main']['humidity'])
    temp_min = (resp['main']['temp_min'])
    temp_max = (resp['main']['temp_max'])
    location = (resp['name'])
    country = (resp['sys']['country'])
   
    lon = (str(resp['coord']['lon']))
    lon = (str(resp['coord']['lon']))
    lon = (str(resp['coord']['lon']))
    OUTPUT_STRING = (
        '{main} and {temp}C in {name}, {country}. {description} with '
        '{wind_speed}m/s winds. Humidity: {humidity}%, sunrise: {sunrise}, '
        'sunset: {sunset}, pressure: {pressure}hPa, visibility: {visibility}'
        ' and lat/lon: {lat}/{lon}.'
    )   
    #return OUTPUT_STRING
    return ("Location: {} lon {}, lat {} Cloud Cover:{} temp: {} Minimum Temp: {} Maximum Temp: {} Humidity: {}%".format(location, lon, lat, sky, temp, temp_min, temp_max, humidity))


def weather(user):
    """get the weather per pre defined user url"""
    user = user.lower()

    if user == "stiv":
        return _stiv_bullshit()
    if user == "specing":
    #   return xml-weather.get_content()
        return (get_weather_slov())
    if user == "disavowed":
        url = 'http://api.openweathermap.org/data/2.5/weather?q=christchurch,NZ&units=metric&appid=b916c6cc293f6a8895951dd365037bac'
        return disavowed_bullshit(url)
        

    location = USER_LOOKUP.get(user)

    if not location:
        return "Berg was too busy killing Aliens to add your location."

    url = ROOT_URL + location
    

    resp = requests.get(url).json()
    weather_data = resp.get("observations", {}).get("data")[0]
    temp_f = _get(weather_data, "air_temp")

    output = {k: _get(weather_data, k) for k, v in weather_data.items() if k in FIELDS}
    output["degree"] = "\N{DEGREE SIGN}"
    output["temp_f"] = "%.2f" % (temp_f * 9 / 5 + 32)
    output["username"] = user

    return _format_output(**output)
import requests 
import xml.etree.ElementTree as ET
import lxml.objectify as objectify 

dict_data = {} 
def xml_to_dict(xml_str):
    """ Convert xml to dict, using lxml v3.4.2 xml processing library, see http://lxml.de/ """
    def xml_to_dict_recursion(xml_object):
        dict_object = xml_object.__dict__
        if not dict_object:  # if empty dict returned
            return xml_object
        for key, value in dict_object.items():
            dict_object[key] = xml_to_dict_recursion(value)
        return dict_object
    xml_obj = objectify.fromstring(xml_str)
    return {xml_obj.tag: xml_to_dict_recursion(xml_obj)}

	# url of rss feed 
def get_weather_slov():
    """ getting slovenia weather"""
    URL = 'http://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_LJUBL-ANA_BEZIGRAD_latest.xml'
    try:
        response = requests.get(URL)
    except:
        return("Unable to reach weather station. Please try again")
    dict_data = (xml_to_dict(response.content))
    data = (dict_data['data']['metData'])
    units = (data['t_var_unit'])
    temp = (data['t_degreesC'])
    humidity = (data['rh'])
    location = (data['domain_longTitle'])
    percent = '%'
    sunrise = (data['sunrise'])
    sunset = (data['sunset'])
    winddirect = (data['dd_decodeText'])
    snow = (data['rr24h_val'])
    pressure = (data['dd_val'])
    degrees = (data['dd_var_unit'])
    wind_speed = (data['ff_val_kmh'])
    wind_units = "kp/h"
    last_update = (data["tsUpdated"])
    precipitation = (data["tsUpdated"])
    return('Location = {} last update = {} Temp = {}{} humidity = {}{} Sunrise = {} sunset = {} wind direction = {} wind speed = {}{} precipitation = {} Air Pressure = {}hPa'.format(location, last_update, temp, units, humidity, percent, sunrise, sunset, winddirect, wind_speed, wind_units, snow, pressure))


def handler(connection, event):
    if event.arguments and event.arguments[0].startswith("my place"):
        connection.privmsg(event.target, weather(event.source.nick))


def get_handlers():
    return (("pubmsg", handler),)
