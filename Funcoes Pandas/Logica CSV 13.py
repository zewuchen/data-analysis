import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Logica CSV 13.csv")

us = df.loc[df["geo_name"] == "United States"]
us = us.sort_values("year")
florida = df.loc[df["geo_name"] == "Florida"]
florida = florida.sort_values("year")

plt.grid()
plt.plot(us["year"], us["total_reimbursements_b"], label="USA")
plt.plot(florida["year"], florida["total_reimbursements_b"], label="Florida")

plt.legend()
plt.show()