from dataclasses import dataclass
import requests

@dataclass
class PyDawa:
    
    srid: str = '25832'
    format: str = 'json'
    struktur: str = 'mini'

    def get_koordinater(self, json_response):
        """Henter koordinater for en given adresse.

        :param json_response: Response fra dawa api. Skal være i json format.

        :returns: En tuple med koordinater.
        :rtype: tuple
        """
        if self.struktur == 'mini':
            return (json_response['x'], json_response['y'])
        elif self.struktur == 'flad':
            return (json_response['vejpunkt_x'], json_response['vejpunkt_y'])
        elif self.struktur == 'nestet':
            return (json_response['adgangsadresse']['adgangspunkt']['koordinater'][0], json_response['adgangsadresse']['adgangspunkt']['koordinater'][1])

@dataclass
class Adressesoeg(PyDawa):
    """Søg efter en adresse i DAR.

        :param q: Adresse, som skal søges efter.
        :param struktur: Strukturen af returneret data fra API. Mulige værdier: "nestet", "flad" eller "mini". Det anbefales at benytte mini-formatet hvis der ikke er behov for den fulde struktur, da dette vil give bedre svartider (DEFAULT mini)
        :param srid: SRID for det koordinatsystem koordinaterne er i (DEFAULT 25832).
        :param format: Mulige værdier json (DEFAULT), geojson (hvor det giver mening), jsonp, ndjson, csv.

        :returns: En liste med svar fra API.
        :rtype: list
    """
    q: str = None
    vejnavn: str = ''
    husnr: str = ''
    postnr: str = ''
    
    def info(self):
        """Henter information om adressen fra DAWA API.
        """
        if self.q == None:
            params = {'vejnavn': self.vejnavn, 'husnr': self.husnr, 'postnr': self.postnr, 'struktur': self.struktur, 'format': self.format, 'srid': self.srid}
            url = 'http://dawa.aws.dk/adresser'
            response = requests.get(url, params=params)
            if self.format == 'json' or self.format == 'geojson':
                response = response.json()
            else:
                response = response.text()
            return response
        else:
            params = {'q': self.q, 'struktur': self.struktur, 'format': self.format, 'srid': self.srid}
            url = 'http://dawa.aws.dk/adresser'
            response = requests.get(url, params=params)
            if self.format == 'json' or self.format == 'geojson':
                response = response.json()
            else:
                response = response.text()
            return response

@dataclass
class Adresseopslag(PyDawa):
    """Henter en adresse fra DAR udfra en adresse id.

    :param id: Adressens unikke id.
    :param struktur: Strukturen af returneret data fra API. Mulige værdier: "nestet", "flad" eller "mini". Det anbefales at benytte mini-formatet hvis der ikke er behov for den fulde struktur, da dette vil give bedre svartider (DEFAULT mini)
    :param srid: SRID for det koordinatsystem koordinaterne er i (DEFAULT 25832).
    :param format: Mulige værdier json (DEFAULT), geojson (hvor det giver mening), jsonp, ndjson, csv.

    :returns: En liste med svar fra API.
    :rtype: list
    """
    id: str = None

    def info(self):
        """Henter information om adressen fra DAWA API.
        """
        params = {'struktur': self.struktur, 'srid': self.srid, 'format': self.format}
        url = 'http://dawa.aws.dk/adresser/' + self.id 
        response = requests.get(url, params=params)
        if self.format == 'json' or self.format == 'geojson':
            response = response.json()
        else:
            response = response.text()
        return response

@dataclass
class Adressevasker(PyDawa):
    """Vasker en adresse og kommer med bedste gæt på en rigtig adresse. 

    :param betegnelse: Adresse, som skal vaskes

    :returns: En eller flere adresser, som bedst matcher svaret
    :rtype: dictionary
    """
    betegnelse: str = None

    def info(self):
        params = {'betegnelse': self.betegnelse}
        url = 'http://dawa.aws.dk/datavask/adresser'
        response = requests.get(url, params=params)
        return response.json()

@dataclass
class Reverse(PyDawa):
    
    koordinater: tuple = ()

    def info(self):
        params = {'x': self.koordinater[0], 'y': self.koordinater[1], 'struktur': self.struktur, 'format': self.format}
        url = 'http://dawa.aws.dk/adgangsadresser/reverse'
        response = requests.get(url, params=params)
        return response.json()