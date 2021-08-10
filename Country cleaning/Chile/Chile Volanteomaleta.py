# %%
import os
import pandas as pd
import numpy as np
import datetime


# %%
datosVM = pd.read_csv(r"D:\Basededatos\Origen\Chile\datos_VM_20.09.20.txt", sep="|", header=None)


# %%
datosVM.head()


# %%
datosVM.columns = ["PATENTE",
                   "SEGMENTO.1",
                   "MARCA",
                   "MODELO / VERSION",
                   "RUT",
                   "NUMERO MOTOR",
                   "AÑO",
                   "NOMBRE",
                   "CANTIDAD"
                   ]
datosVM = datosVM[["PATENTE", "SEGMENTO.1", "MARCA", "MODELO / VERSION", "RUT", "NUMERO MOTOR", "AÑO"]]

# %%
datosVM.drop_duplicates(inplace=True)
datosVM.dropna(how="all", inplace=True)


# %%
datosVM.to_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\datosVM.csv', index=False)


# %%

# %%
datosVM["PATENTE"].isna().sum()
# %%
datosVM.tail(20)
# %%
