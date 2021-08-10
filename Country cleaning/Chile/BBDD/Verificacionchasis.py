# %% IMPORTAR LIBRERIAS
import os
import pandas as pd
import numpy as np
import datetime
from vininfo import Vin # ORIGEN Y MARCA
from pyvin import VIN
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
import html5lib

# %%
datosVM = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\datosVM.csv')
chileBBDD = pd.read_csv(r"D:\Basededatos\Limpioparaunir\chile BBDD.csv")


# %%
verificado = pd.merge(datosVM,
                      chileBBDD[["PATENTE", "NUMERO CHASIS / VIN"]],
                      left_on="PATENTE",
                      right_on="PATENTE",
                      how="left")


# %%
verificado["FABRICANTESEGUNVIN"] = verificado["NUMERO CHASIS / VIN"].map(lambda x: Vin(x).manufacturer)

# %%
condicion = verificado["FABRICANTESEGUNVIN"].notna()
verificado[condicion]


# %%
verificado.dropna(axis=0, subset=["PATENTE"], inplace=True)

# %%
verificado.to_csv(r'D:\Basededatos\Limpioparaunir\chile volanteomaleta.csv', index=False)


# %%
