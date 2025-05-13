import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "suicide-rate-by-country-2024.csv"
data = pd.read_csv(file_path, index_col=0)
df = pd.DataFrame({
    "Country": data["country"],
    "SuicideRate_BothSexes_RatePer100k_2021": data["SuicideRate_BothSexes_RatePer100k_2021"],

})
plt.subplots(1)

print(data["SuicideRate_BothSexes_RatePer100k_2021"])

print(plt.show())