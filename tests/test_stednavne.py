import pytest
from pydawa import Stednavne

@pytest.fixture
def stednavne_object():
    return Stednavne(kommunekode=240)

def test_stednavne_class(stednavne_object):
    assert stednavne_object.kommunekode == 240
    assert stednavne_object.hovedtype == None
    assert stednavne_object.undertype == None

def test_get_data(stednavne_object):
    stednavne_object.hovedtype = 'Bebyggelse'
    bebyggelse = stednavne_object.get_data()
    assert isinstance(bebyggelse, dict)
    assert len(bebyggelse) > 0
