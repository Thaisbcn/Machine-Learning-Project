```python
import pandas as pd
```

# Procés de Recol·lecció de Dades per al Projecte de Predicció de subscripció de Dipòsit a Termini #

## 1. Fonts ##
1. Identificació de Fonts:
Base de dades obtinguda de la recopilació de campanyes de màrqueting telefònic.

### 1.2. Descripció de les Fonts: ###
La base de dades conté registres relatius a dades personals dels client, informació de contacte, resultats de campanyes anteriors, alguna mètrica relativa a la última trucada d'una campanya, com per exemple nombre de contactes o la duració , i dades relacionades en si és morós, o ja té una hipoteca,... 


```python
banc = "bank_dataset.CSV"
df = pd.read_csv(banc)
print(df.info())
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 11162 entries, 0 to 11161
    Data columns (total 17 columns):
     #   Column     Non-Null Count  Dtype  
    ---  ------     --------------  -----  
     0   age        11152 non-null  float64
     1   job        11162 non-null  object 
     2   marital    11157 non-null  object 
     3   education  11155 non-null  object 
     4   default    11162 non-null  object 
     5   balance    11162 non-null  int64  
     6   housing    11162 non-null  object 
     7   loan       11162 non-null  object 
     8   contact    11162 non-null  object 
     9   day        11162 non-null  int64  
     10  month      11162 non-null  object 
     11  duration   11162 non-null  int64  
     12  campaign   11162 non-null  int64  
     13  pdays      11162 non-null  int64  
     14  previous   11162 non-null  int64  
     15  poutcome   11162 non-null  object 
     16  deposit    11162 non-null  object 
    dtypes: float64(1), int64(6), object(10)
    memory usage: 1.4+ MB
    None
    

## 2. Mètodes de recol·lecció de dades ##
### 2.1- Procediments i Eines: ###

Les dades financeres i demogràfiques, com el saldo del compte, préstecs, hipoteques, etc., s'extreuen dels CRM del banc on s'emmagatzemen els perfils dels clients.Aquest CRM també serveix per capturar dades noves de manera centralitzada i eficient.

Les dades es recullen a partir de les campanyes de màrqueting telefònic i les respostes dels clients, la durada de les trucades i altres detalls es registren automàticament.
### 2.2- Freqüència de Recol·lecció: ###

Les campanyes de màrqueting telefònic solen recollir-se en temps real o diàriament després de les trucades
Els informes financers, com el saldo del compte, potser mensualment, trimestralment o semestralment, segons el banc.

### 2.3- Scripts de Descàrrega: ###
banc = "bank_dataset.CSV"

df = pd.read_csv(banc)

print(df.info())

## 3. Format i Estructura de les Dades ##
### 3.1- Tipus de Dades: ###

Aquest resum mostra un DataFramede 11.162 files i 17 columnes. Tot i que totes les columnes marquen que no tenen valors nuls, el número de files és diferent, això implica que hi ha algunes dades mancants. 
Els tipus de dades inclouen dades numèriques de tipos float i enters, dades categòriques format text i algunes d'aquestes que en realitat són booleanes tot i que s'expresen en text. 
   
    1. Columnes amb valors qualitatius o de text:
- job (professió)
- marital (estat civil)
- education (educació)
- contact (mètode de contacte)
- month (mes)
- poutcome (resultat de campanya prèvia)
 
    2. Columnes amb valors quantitatius, de tipus numèric:
- age (edat)
- balance (saldo)
- day (dia del mes en què es va fer el contacte)
- duration (duració de la trucada)
- campaign (nombre de contactes durant la campanya)
- pdays (dies des de l'últim contacte de la campanya anterior)
- previous (nombre de contactes previs)

   3. Columnes de text amb valors que podrien ser binaris (sí/no) ,(0/1):

- default (morositat: pot ser "yes" o "no")
- housing (hipoteca: pot ser "yes" o "no")
- loan (préstec: pot ser "yes" o "no")
- deposit (dipòsit: pot ser "yes" o "no" → l'objectiu de classificació) . AQUESTA ÚLTIMA SERIA LA VARIABLE OBJECTIU DE L'ENTRENAMENT (Y).

### 3.2- Format d'Emmagatzematge: ###

Dades tabulars emmagatzemades en fitxer csv.


## 4. Limitacions de les dades ##

4.1. Qualitat de les dades:  
Algunes variables, com l'edat o l'educació, poden contenir valors nuls o incomplets que poden afectar la precisió del model. És necessari tractar aquests valors abans d'entrenar el model.

4.2. Segmentació de la mostra:  
Hem d'estar segurs que les dades utilitzades representen tots els clients en les proporcions adequades.

4.3. Dades històriques no actualitzades:  
Que podrien  no representar els canvis en el comportament del client. Per exemple si hi han hagut variacions econòmiques o polítiques bancàries...

4.4. Manca de variables rellevants:   
Potser faltaria alguna variable que reflectís la relació personal del client amb el banc o la confiança en el producte.
En relació a l'atenció al client, és complexe capturar el nivell de satisfacció.

4.5. Multicolinealitat:  
En el cas que algunes variables estiguin altament correlacionades (per exemple, la duració de la trucada i la campanya).

## 5. Consideracions sobre Dades Sensibles ##

### 5.1- Tipus de Dades Sensibles:

Degut a la sensibilitat de les dades, aquestes han de ser protegides rigorosament. En relació a la seguretat financera, podria ser utilitzada per activitats fraudulentas i en temes socioeconòmics, necessitem una protecció addicional per evitar la discriminació o l'ús no autoritzat.


Informació Personal Identificable (PII): Edat, ocupació, estat civil, nivell educatiu, contacte.   
Informació Financera: Saldo del compte, detalls de préstecs i hipoteques.  
Informació Sensible de Comportament: Respostes a enquestes de màrqueting, estat civil, resultat de les campanyes.   


### 5.2- Mesures de Protecció:

Encriptació: utilitzant tècniques com AES (Advanced Encryption Standard).  
Dades en trànsit: Utilitza protocols segurs com HTTPS o TLS, en la transmició client-servidor.  
Accés a dades sensibles restringit només a personal autoritzat amb necessitat de conèixer aquestes dades per a fins específics del projecte.  
Anonimització i Pseudonimització: No cal aplicar, doncs ja treballem amb un dataset sense.  
Polítiques de Privadesa i Compliment Normatiu: Compliment del GDPR i altres regulacions si s'escau.
