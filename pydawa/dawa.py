from dataclasses import dataclass
import requests
from urllib.parse import urlencode

@dataclass
class Adressesoeg:
    vejnavn: str
    husnr: str
    postnr: str
    url: str = 'http://dawa.aws.dk/adresser'
    struktur: str = 'mini'
    srid: str = '25832'
    format: str = 'json'

    def info(self):
        params = urlencode({'vejnavn': self.vejnavn, 'husnr': self.husnr, 'postnr': self.postnr, 'struktur': self.struktur, 'format': self.format})
        url = self.url + '?' + params
        response = requests.get(url)
        if self.format == 'json' or self.format == 'geojson':
            response = response.json()
        return response
