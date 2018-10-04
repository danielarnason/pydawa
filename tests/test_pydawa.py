import pytest
from pydawa import Adressesoeg

def test_adressesoeg():
    adresse = Adressesoeg('Rødkildevej', '46', '2400')
    adresse_info = adresse.info()
    assert isinstance(adresse_info, list)
    assert adresse_info[0]['vejnavn'] == 'Rødkildevej'
    assert adresse_info[0]['husnr'] == '46'
    assert adresse_info[0]['postnr'] == '2400'
