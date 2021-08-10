# VIENE DE chile2.PY
# %% IMPORTAR LIBRERIAS
import os
import pandas as pd
import numpy as np
import datetime


# %%
chile2 = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\chile2.csv')


# %% ARREGLAR MODELO
condicion = (chile2["MODELO"] == "PICK") | (chile2["MODELO"] == "PICKUP")
chile2.loc[condicion, "SEGMENTO.1"] = "PICK UP"
chile2.loc[condicion, "MODELO"] = None


# KIA
listamodelo = r'''(SORENTO)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


# CHEVROLET
listamodelo = r'''(CHEVY NOVA|CHEVY TAXI|CHEVY URBAN|CHEVY VAN|CHEVY 500)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]



# HYUNDAI
listamodelo = r'''(SANTA FE|GRAND I-10|GRAND STAREX|GRAND SANTA FE)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


# NEW HOLLAND
listamodelo = r'''(TL 250|TL 200|TL 150|TL 125|TL 110|TL 100|TL 95|TL 95 EXITUS|TL 90|TL 85|TL 85 EXITUS|TL 80|TL 75|TL 75 EXITUS|TL 70|TL 65|TL - 12)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]
chile2["MODELO"].replace({"TL - 12":"Renault 12"}, inplace=True)


# MASSEY FERGUSON
listamodelo = r'''(MF 5650|MF 5320|MF 5310|MF 4299|MF 4292|MF 4283|MF 1175|MF 660|MF 630|MF 399|MF 398|MF 299|MF 298|MF 296|MF 295|MF 292|MF 291|MF 290|MF 285|MF 283|MF 265|MF 275|MF 235|MF 200|MF 155|MF 150|MF 135|MF 125|MF 110|MF 100|MF 95|MF 65)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]
chile2["MODELO"].replace({"TL - 12":"Renault 12"}, inplace=True)


# STAR
listamodelo = r'''(SK DESER|SK SUPER|SK CARGA|SK SUPERTUIS|SK BR200|SK 1722|SK 250|SK 200|SK150|SK 150|SK150-|SK 125|SK110|SK 110|SK 100)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


# JEEP
listamodelo = r'''(GRAND CHEROKEE)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


# FORD
listamodelo = r'''(CARGO 2425|CARGO 1722|CARGO 1721|CARGO 1717|CARGO 1622|CARGO 1618|CARGO 1516|CARGO 1416|CARGO 915|SPACIO|SPAZIO)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]
chile2["MODELO"].replace({"SPACIO":"SPAZIO"}, inplace=True)



# TOYOTA
listamodelo = r'''(ALLION|4 RUNNER|CORONA|LAND CRUISER|FUNCARGO|CALDINA|HI LUX|HILUX|HI ACE|HIACE|TOWNACE)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]

chile2["MODELO"].replace({"VITZ": "YARIS",
                            "IST": "URBAN CRUISER",
                            "IST F L": "URBAN CRUISER",
                            "IST SCION": "URBAN CRUISER",
                            "PLATZ": "YARIS",
                            "ALLEX": "COROLLA",
                            "NOAH": "ESQUIRE",
                            "TOWNACE": "DAIHATSU DELTA",
                            "HI LUX": "HILUX",
                            "HI ACE": "HIACE"}, inplace=True)


# NISSAN
listamodelo = r'''(BLUEBIRD|V16 SENTRA)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]

chile2["MODELO"].replace({"V16 SENTRA": "SENTRA"}, inplace=True)


# HONDA
listamodelo = r'''(GL 1800|GL 1500|GL 1200|GL 1000|GL 550|GL 500|GL 450|GL 420|GL 400|GL 350|GL 320|GL 305|GL 244|GL 200|GL 150|GL 125|GL 110|GL 100| GL 90)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(CG TODAY|CG STRADA|CG TITAN|CG 150|CG  125|CG 125|CG 110|CG 4)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]

listamodelo = r'''(ML 430|ML 400|ML 350|ML 320|ML 300|ML 280|ML 270|ML 200|ML - 150|ML 150|ML - 125|ML 125|ML 110|ML 63)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]



# MONDIAL
listamodelo = r'''(MD 920|MD 200|MD 150|MD 125|MD 100)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


# MONTANA
listamodelo = r'''(MC 125|MC 110|MC 100)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]



# KENTON
listamodelo = r'''(VIVA 110|GTR Z|GTR 200|GTR 150|GL 90|GL 10|GL 1300)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


# FIAT
listamodelo = r'''(PREMIO|UNO|STRADA|STRADA WORKING|STRADA ADVENTURE|STRADA HARD|STRADA FIRE)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]

chile2["MODELO"].replace({"PREMIO": "DUNA"}, inplace=True)


# VOLKSWAGEN
listamodelo = r'''(GOL|ESCARABAJO|SUNNY)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]

chile2["MODELO"].replace({"SUNNY": "SENTRA"}, inplace=True)


# MITSUBISHI
chile2["MODELO"].replace({"PAJERO": "MONTERO"}, inplace=True)


# LEOPARD
listamodelo = r'''(HT 200|HT 150)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


# SUZUKI
listamodelo = r'''(GRAND VITARA)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


# KAWAZAKI
listamodelo = r'''(KH 200|KH 150|KH 125|KH 110|KH 100|KH 90)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


# MERCEDES BENZ
listamodelo = r'''(SPRINTER|SPRINTER F3000|SPRINTER 515|SPRINTER 415|SPRINTER 313|SPRINTER 310|SPRINTER 308|SPRINTER 208)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]



# MODELOS DE UNA SOLA LETRA
listamodelo = r'''(C 09670|C 6503|C 1414|C 650|C 350|C 320|C 300|C 290|C 280|C 272|C 270|C 250|C 240|C 230|C 220|C 200|C 190|C 180|C 150|C 125|C 110|C 90|C 70|C 63|C 60|C 43|C 36|C 30|C 25|C 20|C 15|C 14|C 10|C 4|C 2)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(L 46507|L 9000|L 8000|L 2221|L  2213|L  2013|L 1620|L 1618|L 1614|L 1520|L 1519|L 1518|L 1514|L 1513|L 1414|L 1318|L 1316|L 1313|L 1214|L 1118|L 1113|L 915|L 708|L 608|L 524|L 508|L 300|L 200|L 111|L 100|L -608|L -1516)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(GTS SUPER|GTS DISCOVERY|GTS 1600S|GTS 300|GTS 200|GTS 150)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(GLX 150)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(3)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]
chile2["MODELO"].replace({"3": None}, inplace=True)


listamodelo = r'''(GTX 600|GTX 400|GTX 150|GTX 21)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(F 14000|F 12000|F 11000|F 8000|F 7000|F 5000|F 4000|F 2574|F 1000|F 800|F 700|F 650|F 600|F 500|F 250|F 150|F 100|F 89|F 86|F 85|F 80|F 70|F 12|F 10)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(D 14000|D 12000|D 900|D 800|D 750|D 700|D 500|D 400|D 200|D 110|D 100|D 60|D 22|D 21|D 16|D 8|D 6|D 4)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(GRAND NOMADE|GRAND CARNIVAL|GRAND DINK|GRAND SALOON|GRAND TIGER|GRAND AM|GRAND TOWN COUNTRY)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(LO 812|LO 8124|LO 8094|LO 6080|LO 1114|LO 915|LO 914|LO 814|LO 812|LO 809|LO 712|LO 708|LO 608)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(B 700|B 7000|B 2600|B 2500|B 2200|B 2000|B 614|B 600|B 500|B 210|B 160|B 110|B 58|B 42|B 20|B 18|B 16|B 10)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(S 500|S 215|S 170|S 160|S 85|S 70|S 60|S 40|S 10)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(SK 410|SK 408|SK 210)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(AK 6)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(XR 650|XR 600|XR 500|XR 400|XR 250|XR 200|XR 125|XR 100)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]


listamodelo = r'''(XL 1000|XL 650|XL 250|XL 185|XL 125|XL 75)'''
chile2["MODELO2"] = chile2["MODELO / VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = chile2["MODELO2"].notna()
chile2.loc[condicion, "MODELO"] = chile2.loc[condicion, "MODELO2"]
chile2 = chile2[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR", "MERCADO", "CANTIDAD", "MOTOR", "MODELO"]]



# %%
chile2.to_csv(r'D:\Basededatos\Limpioparaunir\chile2.csv', index=False)


# %%
dict(chile2["MODELO"].value_counts())


# %%
condicion = chile2["MODELO"] == "XL"
chile2[condicion]


# %%
dict(chile2[condicion]["MODELO / VERSION"].value_counts())



# %%
