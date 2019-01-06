import requests


ROOT_URL = "http://www.bom.gov.au/fwo/"
WEATHER_TEXT = (
    "{name} -- Location {username}'s Place --Time {local_date_time} -- The "
    "Wind is from the {wind_dir} -- Wind speed {wind_spd_kt} KPH -- Wind "
    "gusts {gust_kmh} KPH -- Air temps is {air_temp}{degree}C -- {temp_f}"
    "{degree}F -- Relative Humidity is {rel_hum}% -- Air Pressure is "
    "{press}kPa -- Rain {rain_trace}"
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
}
USER_LOOKUP = {
    "berg": "IDN60801/IDN60801.94785.json",
    "bluemaxima": "IDN60801/IDN60801.94733.json",
    "dodobrain": "IDQ60901/IDQ60901.94575.json",
    "thearm": "IDN60801/IDN60801.94592.json",
    "ukn0me": "IDW60801/IDW60801.95610.json",
    "dooblynoobly": "IDQ60901/IDQ60901.94576.json",
    "oobz": "IDQ60901/IDQ60901.94576.json",
    "sydneyi": "IDN60901/IDN60901.94768.json",
    "duoi": "IDN60801/IDN60801.95704.json",
    "mwsb": "IDN60801/IDN60801.94926.json",
    "dudz": "IDN60801/IDN60801.95757.json",
    "chris": "IDN60901/IDN60901.94768.json",
    "mcspud": "IDV60901/IDV60901.95936.json",
    "wyoung": "IDN60801/IDN60801.94749.json",
    "win32user":"IDN60901/IDN60901.94765.json",
    "orlock": "IDV60801/IDV60801.94864.json",
    "pebbles": "IDV60901/IDV60901.94872.json",
}


def _stiv_bullshit():
    url = "https://api.weather.gov/stations/KIGQ/observations/current"
    return url


def _get(d, item):
    return d.get(item, "")


def _format_output(**values):
    return WEATHER_TEXT.format(**values)


def _calculate_temp_in_c(temp):
    return str((temp * 9 / 5.0 + 32) if temp else "")


def weather(user, text):
    user = user.lower()
    '''words = text.split(":")[2].strip("\r\n")
    words = words.split()
    words = words[0] + words[1]
    print(words)
    if words != "myplace":
        return'''
    if user == "stiv":
        return _stiv_bullshit()
    url = ROOT_URL + USER_LOOKUP.get(user)
    if not url:
        return "Berg was too busy sucking dongs to add your location."

    resp = requests.get(url).json()
    d = resp.get("observations", {}).get("data")[-1]

    temp_f = _get(d, "air_temp")
    temp_c = _calculate_temp_in_c(temp_f)

    output = {k: _get(d, k) for k, v in d.items() if k in FIELDS}
    output["degree"] = "\N{DEGREE SIGN}"
    output["temp_f"] = "%.2f" % (temp_f * 9 / 5 + 32)
    output["username"] = user

    return _format_output(**output)
