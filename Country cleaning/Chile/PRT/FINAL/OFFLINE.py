# %%
import os
import pandas as pd
import numpy as np
import datetime

# %%
offlineRB1 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\OfflineRB1.csv")
offlineRB2 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\OfflineRB2.csv")
offlineRB3 = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\Limpio\OfflineRB3.csv")

# %%
offline = pd.concat([offlineRB1,
                     offlineRB2,
                     offlineRB3], ignore_index=True, join='outer')


# %%
offline = offline[["PPU", "MARCA", "MODELO", "ANO_FABRICACION", "NUM_MOTOR", "NUM_CHASIS","VIN"]]

# %%
offline.drop_duplicates(subset="PPU", inplace=True)

# %%
offline.info()
# %%
offline.to_csv(r'F:\Trabajo\Promotive\Chile\PRT\FINAL\offline.csv', index=False)

# %%
