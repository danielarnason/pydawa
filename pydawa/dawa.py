from dataclasses import dataclass
import requests
from urllib.parse import urlencode

@dataclass
class Adressesoeg:
    """Søg efter en adresse i DAR.

        :param vejnavn: Vejnavnet på den søgte adresse.
        :param husnr: Husnummeret på den søgte adresse.
        :param postnr: Postnummeret på den søgte adresse(DEFAULT None).
        :param struktur: Strukturen af returneret data fra API. Mulige værdier: "nestet", "flad" eller "mini". Det anbefales at benytte mini-formatet hvis der ikke er behov for den fulde struktur, da dette vil give bedre svartider (DEFAULT mini)
        :param srid: SRID for det koordinatsystem koordinaterne er i (DEFAULT 25832).
        :param format: Mulige værdier json (DEFAULT), geojson (hvor det giver mening), jsonp, ndjson, csv.

        :returns: En dictionary med svar fra API.
        :rtype: dictionary
    """
    vejnavn: str
    husnr: str
    postnr: str 
    struktur: str = 'mini'
    srid: str = '25832'
    format: str = 'json'

    def info(self):
        """Henter information om adressen fra DAWA API.
        """
        params = urlencode({'vejnavn': self.vejnavn, 'husnr': self.husnr, 'postnr': self.postnr, 'struktur': self.struktur, 'format': self.format, 'srid': self.srid})
        url = 'http://dawa.aws.dk/adresser?' + params
        response = requests.get(url)
        if self.format == 'json' or self.format == 'geojson':
            response = response.json()
        else:
            response = response.text()
        return response

@dataclass
class Adresseopslag:
    """Henter en adresse fra DAR udfra en adresse id.

    :param id: Adressens unikke id.
    :param struktur: Strukturen af returneret data fra API. Mulige værdier: "nestet", "flad" eller "mini". Det anbefales at benytte mini-formatet hvis der ikke er behov for den fulde struktur, da dette vil give bedre svartider (DEFAULT mini)
    :param srid: SRID for det koordinatsystem koordinaterne er i (DEFAULT 25832).
    :param format: Mulige værdier json (DEFAULT), geojson (hvor det giver mening), jsonp, ndjson, csv.

    :returns: En dictionary med svar fra API.
    :rtype: dictionary
    """
    id: str
    srid: str = '25832'
    format: str = 'json'
    struktur: str = 'mini'

    def info(self):
        """Henter information om adressen fra DAWA API.
        """
        params = urlencode({'struktur': self.struktur, 'srid': self.srid, 'format': self.format})
        url = 'http://dawa.aws.dk/adresser/' + self.id + '?' + params
        response = requests.get(url)
        if self.format == 'json' or self.format == 'geojson':
            response = response.json()
        else:
            response = response.text()
        return response

@dataclass
class Adressevasker:
    """Vasker en adresse og kommer med bedste gæt på en rigtig adresse. 

    :param betegnelse: Adresse, som skal vaskes

    :returns: En eller flere adresser, som bedst matcher svaret
    :rtype: dictionary
    """
    betegnelse: str

    def info(self):
        params = urlencode({'betegnelse': self.betegnelse})
        url = 'http://dawa.aws.dk/datavask/adresser?' + params
        response = requests.get(url)
        return response.json()