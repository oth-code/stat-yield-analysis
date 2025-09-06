import numpy as np
import pandas as pd


rng = np.random.default_rng(42)
# 500 mesures ~ N(5.00V, 0.07V) + 10 outliers légers
good = rng.normal(loc=5.00, scale=0.07, size=500)
outliers = rng.normal(loc=5.12, scale=0.03, size=10)
data = np.concatenate([good, outliers])

df = pd.DataFrame({"voltage_V": np.round(data, 4)})
df.to_csv("data/measurements.csv", index=False)
print("Saved -> data/measurements.csv, rows:", len(df))