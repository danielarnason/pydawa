import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from .dawa import *
import csv

@dataclass
class Geokoder:
    """En Class, som tager i mod en sti til en csv eller en xlsx fil, og kan geokode den.

    Parameters:
        filepath (str): Placeringen af filen.
    """
    filepath: str = None
    cols: None = None

    def __post_init__(self):
        if type(self.filepath) == str:
            self.filepath = Path(self.filepath)
            self.extension = self.filepath.suffix

    def progbar(self, curr, total, full_progbar):
        frac = curr / total
        filled_progbar = round(frac * full_progbar)
        print('\r', '#' * filled_progbar + '-' * (full_progbar - filled_progbar), f'[{frac:>7.2%}]', end='')

    def geocode_df(self, dataframe):
        total_len = len(dataframe.index)
        for index, row in dataframe.iterrows():
            search_string = ' '.join([str(row[col]) for col in self.cols])
            adresse = Adressesoeg(q=search_string)
            adresse_data = adresse.info()
            if len(adresse_data) > 0:
                koordinat = adresse.get_koordinater(adresse_data[0])
                dataframe.set_value(index, 'x', koordinat[0])
                dataframe.set_value(index, 'y', koordinat[1])
            else:
                adresse_vask = Adressevasker(betegnelse=search_string)
                response_vask = adresse_vask.info()
                adr_id = response_vask['resultater'][0]['adresse']['id']
                rigtig_adresse = Adresseopslag(id=adr_id)
                rigtig_adresse_data = rigtig_adresse.info()
                try:
                    koordinat = rigtig_adresse.get_koordinater(rigtig_adresse_data)
                    dataframe.set_value(index, 'x', koordinat[0])
                    dataframe.set_value(index, 'y', koordinat[1])
                except:
                    dataframe.set_value(index, 'x', 'NaN')
                    dataframe.set_value(index, 'y', 'NaN')
            self.progbar(index + 1, total_len, 100)
        return dataframe

    def geokod_file(self, save=False):

        if self.filepath == None:
            raise Exception(f'filepath ikke defineret!')
        elif not self.filepath.exists():
            raise FileNotFoundError(f'{self.filepath} findes ikke!')

        if self.extension == '.csv':
            sep = self.find_csv_sep()
            df = pd.read_csv(self.filepath, sep=sep)
            df_geokod = self.geocode_df(df)
            if save == True:
                df_geokod.to_csv(str(self.filepath.parent.joinpath(f'{self.filepath.stem}_geokodet{self.filepath.suffix}')))
            else:
                return df_geokod

        elif self.extension =='.xlsx':
            df = pd.read_excel(self.filepath)
            df_geokod = self.geocode_df(df)
            if save == True:
                df_geokod.to_excel(str(self.filepath.parent.joinpath(f'{self.filepath.stem}_geokodet{self.filepath.suffix}')))
            else:
                return df_geokod

    def find_csv_sep(self):
        sniffer = csv.Sniffer()
        with open(self.filepath, 'r') as f:
            line = f.readline()
            dialect = sniffer.sniff(line)
        return dialect.delimiter