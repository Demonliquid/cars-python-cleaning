# %%
import os
import pandas as pd
import numpy as np
import datetime

# %%
convencionalRA12 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\convencionalRA12.csv")
convencionalRB = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\convencionalRB.csv")
offlineRA1RM = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\OfflineRA1RM.csv")
offlineRA12 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\OfflineRA12.csv")


# %%
otros = pd.concat([convencionalRA12,
                     convencionalRB,
                     offlineRA1RM,
                     offlineRA12], ignore_index=True, join='outer')


# %%
otros = otros[["PPU", "MARCA", "MODELO", "ANO_FABRICACION", "NUM_MOTOR", "NUM_CHASIS","VIN"]]

# %%
otros.drop_duplicates(subset="PPU", inplace=True)

# %%
otros.info()
# %%
otros.to_csv(r'F:\Trabajo\Promotive\Chile\PRT\FINAL\otros.csv', index=False)

# %%
