import pytest
import pandas as pd
from pydawa import Geokoder
from pathlib import Path
import csv

@pytest.fixture(scope='session')
def dataframe():
    adresser = [
        'Dronning Dagmars Vej 200, 3650 Ølstykke',
        'Rødkildevej 46, 2400 København',
    ]
    df = pd.DataFrame(data=adresser, columns=['Adresse'])
    return df

@pytest.fixture(scope='session')
def csv_file(dataframe, tmpdir_factory):
    csv_filename = str(tmpdir_factory.mktemp('data').join('test_data.csv'))
    dataframe.to_csv(csv_filename, sep=';')
    return csv_filename 

@pytest.fixture(scope='session')
def xlsx_file(dataframe, tmpdir_factory):
    xlsx_filename = str(tmpdir_factory.mktemp('data').join('test_data.xlsx'))
    dataframe.to_excel(xlsx_filename)
    return xlsx_filename 

@pytest.fixture(scope='session')
def geokoder_object_csv(csv_file):
    geokoder = Geokoder(csv_file, cols=['Adresse'])
    return geokoder

@pytest.fixture(scope='session')
def geokoder_object_xlsx(xlsx_file):
    geokoder = Geokoder(xlsx_file, cols=['Adresse'])
    return geokoder

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        geokoder = Geokoder('c:/test.csv', cols=['Adresse'])

def test_geokod_csv_save_false(geokoder_object_csv):
    df_geokod = geokoder_object_csv.geokod_file()
    assert isinstance(df_geokod, pd.DataFrame)
    assert 'x' in df_geokod.columns
    assert 'y' in df_geokod.columns

def test_geokod_csv_save_file(geokoder_object_csv):
    geokoder_object_csv.geokod_file(save=True)
    saved_file = str(geokoder_object_csv.filepath.parent.joinpath(f'{geokoder_object_csv.filepath.stem}_geokodet{geokoder_object_csv.filepath.suffix}'))
    assert Path(saved_file).exists

def test_geokod_xlsx_save_false(geokoder_object_xlsx):
    df_geokod = geokoder_object_xlsx.geokod_file()
    assert isinstance(df_geokod, pd.DataFrame)
    assert 'x' in df_geokod.columns
    assert 'y' in df_geokod.columns

def test_geokod_xlsx_save_file(geokoder_object_xlsx):
    geokoder_object_xlsx.geokod_file(save=True)
    saved_file = str(geokoder_object_xlsx.filepath.parent.joinpath(f'{geokoder_object_xlsx.filepath.stem}_geokodet{geokoder_object_xlsx.filepath.suffix}'))
    assert Path(saved_file).exists

def test_csv_find_sep(geokoder_object_csv):
    sep = geokoder_object_csv.find_csv_sep()
    assert sep == ';'