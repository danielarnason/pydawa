PyDawa
======
En simple API wrapper omkring Danmarks Adressers Web API (DAWA).

Formålet med dette modul er at give nem adgang til DAWA i Python. Grunden til, at jeg begyndte at arbejde på dette modul er, at jeg havde skrevet et par scripts i python, der brugte API'et, men der var ingen "nem" adgang til det. Plus, jeg var nysgerrig over, om jeg kunne skrive et modul og uploade til pypi.

Det her projekt er et "work in progress", så jeg kommer til at tilføje funktionalitet, når jeg har brug for den. Jeg håber, at folk har lyst til at hjælpe med det.

Afhængigheder
* Requests

Installation
----
Installer med pip:

```$ pip install pydawa```

Brug
-----

Indtil videre, består modulet kun af tre classer:

1. Adressesoeg
2. Adresseopslag
3. Adressevasker

### Adressesoeg()
Søg efter en adresse med vejnavn, husnr og postnummer.

```python
import pydawa

adresse = pydawa.Adressesoeg(vejnavn, husnr, postnr)
response = adresse.info()
```
`info()` metoden henter data fra dawa api'et og returnerer en dictionary med respons.

### Adresseopslag
Søg efter en adresse med adressens unikke id.

```python
import pydawa

adresse = pydawa.Adresseopslag(id)
response = adresse.info()
```
`info()` metoden henter data fra dawa api'et og returnerer en dictionary med respons.

### Adressevasker
Datavask af adressebetegnelse. Modtager en adressebetegnelse og returnerer en eller flere adresser, der bedst matcher.

```python
import pydawa

adresse = pydawa.Adressevasker(adressebetegnelse)
response = adresse.info()
```