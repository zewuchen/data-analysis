import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({"x":["2016Q1", "2016Q2", "2016Q3", "2016Q4", "2017Q1"],
                   "Android":[83.4, 87.6, 86.8, 81.4, 85],
                   "iOS":[15.4, 11.7, 12.5, 18.2, 14.7],
                   "WindowsPhone":[0.8, 0.4, 0.3, 0.2, 0.1],
                   "Others":[0.4, 0.3, 0.4, 0.2, 0.1]})

plt.plot("x", "Android", data= df, marker="x", color="r", linewidth=2, linestyle="dashed")
plt.plot("x", "iOS", data= df, marker="o", color="b", linewidth=2, linestyle="dotted")
plt.plot("x", "WindowsPhone", data= df, color="g", linewidth=6, linestyle="dashed")
plt.plot("x", "Others", data= df, marker="o", color="orange")
plt.legend()