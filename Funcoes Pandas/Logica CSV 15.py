import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Logica CSV 15.csv")

infarto = df.loc[df["cohort_name"] == "Acute Myocardial Infarction"]
infarto = infarto.sort_values("year")

pneumonia = df.loc[df["cohort_name"] == "Pneumonia"]
pneumonia = pneumonia.sort_values("year")

heart = df.loc[df["cohort_name"] == "Congestive Heart Failure"]
heart = heart.sort_values("year")

index = heart["year"]
bar_width = 0.20
opacity = 0.8

rects1 = plt.bar(index, infarto["patients_in_cohort"], bar_width, alpha=opacity, color='b',label='Infarto')
rects2 = plt.bar(index + bar_width, pneumonia["patients_in_cohort"],bar_width,alpha=opacity,color='g',label='Pneumonia')
rects3 = plt.bar(index + 2* bar_width, heart["patients_in_cohort"],bar_width,alpha=opacity,color='black',label='Coração')

plt.xlabel('Anos')
plt.ylabel('Pacientes')

plt.title('Doenças e pacientes')

plt.legend()
plt.show()