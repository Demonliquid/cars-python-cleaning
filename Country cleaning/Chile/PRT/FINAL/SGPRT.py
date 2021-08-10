# %%
import os
import pandas as pd
import numpy as np
import datetime

# %%
sgprtRA1 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\SGPRT RA1.csv")
sgprtRB2 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\SGPRT RB2.csv")
sgprtRB3 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\SGPRT RB3.csv")
sgprtRB4 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\SGPRT RB4.csv")
sgprtRB5 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\SGPRT RB5.csv")
sgprtRB6 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\SGPRT RB6.csv")
sgprtRB7 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\SGPRT RB7.csv")
sgprtRB8 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\SGPRT RB8.csv")
sgprtRB9 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\SGPRT RB9.csv")


# %%
sgprtRB = pd.concat([sgprtRA1,
                     sgprtRB2,
                     sgprtRB3,
                     sgprtRB4,
                     sgprtRB5,
                     sgprtRB6,
                     sgprtRB7,
                     sgprtRB8,
                     sgprtRB9], ignore_index=True, join='outer')


# %%
sgprtRB = sgprtRB[["PPU", "MARCA", "MODELO", "ANO_FABRICACION", "NUM_MOTOR", "NUM_CHASIS","VIN"]]

# %%
sgprtRB.drop_duplicates(subset="PPU", inplace=True)

# %%
sgprtRB.info()
# %%
sgprtRB.to_csv(r'F:\Trabajo\Promotive\Chile\PRT\FINAL\sgprtRB.csv', index=False)


# %%
