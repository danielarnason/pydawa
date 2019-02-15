import pytest
from pydawa import Adressesoeg, Adresseopslag, Adressevasker, Reverse

def test_adressesoeg_opslit():
    adresse = Adressesoeg(vejnavn='Rødkildevej', husnr='46', postnr='2400')
    adresse_info = adresse.info()
    assert isinstance(adresse_info, list)
    assert adresse_info[0]['vejnavn'] == 'Rødkildevej'
    assert adresse_info[0]['husnr'] == '46'
    assert adresse_info[0]['postnr'] == '2400'

def test_adressesoeg_q():
    adresse = Adressesoeg(q='Rødkildevej 46, 2400 København')
    adresse_info = adresse.info()
    assert isinstance(adresse_info, list)
    assert adresse_info[0]['vejnavn'] == 'Rødkildevej'
    assert adresse_info[0]['husnr'] == '46'
    assert adresse_info[0]['postnr'] == '2400'

def test_adresseopslag():
    adresse = Adresseopslag(id='0255b942-f3ac-4969-a963-d2c4ed9ab943')
    adresse_info = adresse.info()
    assert isinstance(adresse_info, dict)
    assert adresse_info['vejnavn'] == 'Mosestien'
    assert adresse_info['husnr'] == '25'
    assert adresse_info['postnr'] == '6430'

def test_adressevasker():
    adresse = Adressevasker(betegnelse='Dronning dagmarsvej 200 3650 ølstyke')
    adresse_info = adresse.info()
    assert isinstance(adresse_info, dict)
    assert 'kategori' in adresse_info
    assert isinstance(adresse_info['resultater'], list)

def test_get_koordinater():
    adresse = Adressesoeg(q='Rødkildevej 46, 2400 København')
    adresse_info = adresse.info()
    koordinater = adresse.get_koordinater(adresse_info[0])
    assert isinstance(koordinater, tuple)
    assert isinstance(koordinater[0], float)
    assert isinstance(koordinater[1], float)

def test_reverse():
    koordinater = (12.58, 55.68)
    reverse_geokod = Reverse(koordinater=koordinater).info()
    assert isinstance(reverse_geokod, dict)
    assert reverse_geokod['id'] == '0a3f507a-f1ad-32b8-e044-0003ba298018'