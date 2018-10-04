import pytest
from pydawa import Adressesoeg, Adresseopslag

def test_adressesoeg():
    adresse = Adressesoeg('Rødkildevej', '46', '2400')
    adresse_info = adresse.info()
    assert isinstance(adresse_info, list)
    assert adresse_info[0]['vejnavn'] == 'Rødkildevej'
    assert adresse_info[0]['husnr'] == '46'
    assert adresse_info[0]['postnr'] == '2400'

def test_adresseopslag():
    adresse = Adresseopslag('0255b942-f3ac-4969-a963-d2c4ed9ab943')
    adresse_info = adresse.info()
    assert isinstance(adresse_info, dict)
    assert adresse_info['vejnavn'] == 'Mosestien'
    assert adresse_info['husnr'] == '25'
    assert adresse_info['postnr'] == '6430'