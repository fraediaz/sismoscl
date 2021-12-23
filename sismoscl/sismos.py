import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import json
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen


def sismos(m=None):
    url = ""
    if m is not None:
        if type(m) is int:
            if m >= 12:
                return "Afortunadamente, no hay registros"
            url = "https://api.xor.cl/sismo/recent?magnitude=" + str(m)
            response = urlopen(url)
            data_json = json.loads(response.read())
            eventos = data_json["events"]
            return eventos
        else:
            print("Debes ingresar un número")
    else:
        url = "https://api.xor.cl/sismo/recent"
        response = urlopen(url)
        data_json = json.loads(response.read())
        eventos = data_json["events"]
        return eventos


print(sismos())
