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


def weather(user):
    """get the weather per pre defined uer url"""
    user = user.lower()

    if user == "stiv":
        return _stiv_bullshit()
    location = USER_LOOKUP.get(user)

    if not location:
        return "Berg was too busy sucking dongs to add your location."

    url = ROOT_URL + location

    resp = requests.get(url).json()
    weather_data = resp.get("observations", {}).get("data")[0]
    temp_f = _get(weather_data, "air_temp")

    output = {k: _get(weather_data, k) for k, v in weather_data.items() if k in FIELDS}
    output["degree"] = "\N{DEGREE SIGN}"
    output["temp_f"] = "%.2f" % (temp_f * 9 / 5 + 32)
    output["username"] = user

    return _format_output(**output)


def handler(connection, event):
    if event.arguments and event.arguments[0].startswith("my place"):
        connection.privmsg(event.target, weather(event.source.nick))


def get_handlers():
    return (("pubmsg", handler),)
