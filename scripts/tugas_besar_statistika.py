# installation extension
!pip install pandas-summary
!pip install pandas-profiling

# import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling
import numpy as np
from scipy import stats
from pandas_summary import DataFrameSummary
import matplotlib.patheffects as path_effects

# set up for display
pd.set_option("display.max_columns", 200)
plt.style.use("ggplot")

# read data
health_care_df = pd.read_csv("https://raw.githubusercontent.com/SyahrezaAdnan/Tugas-Besar-Statistika-data-healthcare-dataset-stroke-data/main/data%20set/data%20healthcare-dataset-stroke-data.csv")

# show data
health_care_df

# show summary of data
health_care_df.describe()

# show summary of each variable
health_care_df.profile_report()

# create histogram for some variable
fig, (graph1) = plt.subplots(figsize = (15, 5))
sns.histplot(data = health_care_df, x = "age", kde = True, ax = graph1)
graph1.set_title("Age Histogram")

fig, (graph1) = plt.subplots(figsize = (15, 5))
sns.histplot(data = health_care_df, x = "avg_glucose_level", kde = True, ax = graph1)
graph1.set_title("Average Glucose Level Histogram")

fig, (graph1) = plt.subplots(figsize = (15, 5))
sns.histplot(data = health_care_df, x = "bmi", kde = True, ax = graph1)
graph1.set_title("Body Mass Index Histogram")

# create boxplot for some variable
# function for labeling median
def add_median_labels(ax, fmt='.1f'):
    lines = ax.get_lines()
    boxes = [c for c in ax.get_children() if type(c).__name__ == 'PathPatch']
    lines_per_box = int(len(lines) / len(boxes))
    for median in lines[4:len(lines):lines_per_box]:
        x, y = (data.mean() for data in median.get_data())
        # choose value depending on horizontal or vertical plot orientation
        value = x if (median.get_xdata()[1] - median.get_xdata()[0]) == 0 else y
        text = ax.text(x, y, f'{value:{fmt}}', ha='center', va='center',
                       fontweight='heavy', color='white')
        # create median-colored border around white text for contrast
        text.set_path_effects([
            path_effects.Stroke(linewidth=3, foreground=median.get_color()),
            path_effects.Normal(),
        ])

# show Stroke and Average Glucose Level Box Plot
fig, ((graph1, graph2, graph3, graph4)) = plt.subplots(4,1, figsize = (10,35))

ax1 = sns.boxplot(data=health_care_df, x='stroke', y='avg_glucose_level', ax = graph1)
graph1.set_title("Stroke and Average Glucose Level Box Plot")
add_median_labels(ax1)

ax2 = sns.boxplot(data=health_care_df, x='stroke', y='avg_glucose_level', hue="smoking_status", ax = graph2)
graph2.set_title("Stroke and Average Glucose Level Box Plot")
add_median_labels(ax2)

ax3 = sns.boxplot(data=health_care_df, x='stroke', y='avg_glucose_level', hue="Residence_type", ax = graph3)
graph3.set_title("Stroke and Average Glucose Level Box Plot")
add_median_labels(ax3)

ax4 = sns.boxplot(data=health_care_df, x='stroke', y='avg_glucose_level', hue="hypertension", ax = graph4)
graph4.set_title("Stroke and Average Glucose Level Box Plot")
add_median_labels(ax4)

plt.show()

# show Stroke and Body Mass Index Box Plot
fig, ((graph1, graph2, graph3, graph4)) = plt.subplots(4,1, figsize = (10,35))

ax1 = sns.boxplot(data=health_care_df, x='stroke', y='bmi', ax = graph1)
graph1.set_title("Stroke and Body Mass Index Box Plot")
add_median_labels(ax1)

ax2 = sns.boxplot(data=health_care_df, x='stroke', y='bmi', hue="smoking_status", ax = graph2)
graph2.set_title("Stroke and Body Mass Index Box Plot")
add_median_labels(ax2)

ax3 = sns.boxplot(data=health_care_df, x='stroke', y='bmi', hue="Residence_type", ax = graph3)
graph3.set_title("Stroke and Body Mass Index Box Plot")
add_median_labels(ax3)

ax4 = sns.boxplot(data=health_care_df, x='stroke', y='bmi', hue="hypertension", ax = graph4)
graph4.set_title("Stroke and Body Mass Index Box Plot")
add_median_labels(ax4)

plt.show()

# show Stroke and Age Box Plot
fig, ((graph1, graph2, graph3, graph4)) = plt.subplots(4,1, figsize = (10,35))

ax1 = sns.boxplot(data=health_care_df, x='stroke', y='age', ax = graph1)
graph1.set_title("Stroke and Age Box Plot")
add_median_labels(ax1)

ax2 = sns.boxplot(data=health_care_df, x='stroke', y='age', hue="smoking_status", ax = graph2)
graph2.set_title("Stroke and Age Box Plot")
add_median_labels(ax2)

ax3 = sns.boxplot(data=health_care_df, x='stroke', y='age', hue="Residence_type", ax = graph3)
graph3.set_title("Stroke and Age Box Plot")
add_median_labels(ax3)

ax4 = sns.boxplot(data=health_care_df, x='stroke', y='age', hue="hypertension", ax = graph4)
graph4.set_title("Stroke and Age Box Plot")
add_median_labels(ax4)

plt.show()

# create line plot for some variable
sns.relplot(x='age', y='stroke', data=health_care_df, kind='line', height = 4, aspect = 4)
sns.relplot(x='age', y='bmi', data=health_care_df, kind='line', height = 4, aspect = 4)
sns.relplot(x='age', y='avg_glucose_level', data=health_care_df, kind='line', height = 4, aspect = 4)
sns.relplot(x='bmi', y='stroke', data=health_care_df, kind='line', height = 4, aspect = 4)
sns.relplot(x='bmi', y='heart_disease', data=health_care_df, kind='line', height = 4, aspect = 4)
sns.relplot(x='avg_glucose_level', y='stroke', data=health_care_df, kind='line', height = 4, aspect = 4)
sns.relplot(x='avg_glucose_level', y='hypertension', data=health_care_df, kind='line', height = 4, aspect = 4)

# create scatter plot for some variable
fig, ((graph1, graph2), (graph3, graph4), (graph5, graph6)) = plt.subplots(3,2, figsize = (15, 20))
sns.scatterplot(data = health_care_df, x = "age", y = "hypertension", ax = graph1)
graph1.set_title("Age and Hypertension Scatterplot")
sns.scatterplot(data = health_care_df, x = "age", y = "heart_disease", ax = graph2)
graph2.set_title("Age and Hearth Disease Scatterplot")
sns.scatterplot(data = health_care_df, x = "age", y = "avg_glucose_level", ax = graph3)
graph3.set_title("Age and Average Glucose Level Scatterplot")
sns.scatterplot(data = health_care_df, x = "age", y = "bmi", ax = graph4)
graph4.set_title("Age and BMI Scatterplot")
sns.scatterplot(data = health_care_df, x = "age", y = "stroke", ax = graph5)
graph5.set_title("Age and stroke Scatterplot")

# create correlation matrix and heatmap of the data
plt.figure(figsize=(16, 8))
sns.set(font_scale=1.3)
heatmap = sns.heatmap(health_care_df.corr(), vmin=-1, vmax=1, annot=True)

heatmap.set_title('Correlation Heatmap Health Care Data and Stroke Data', fontdict={'fontsize':16, 'fontweight': 'heavy'}, pad=10);

# test the correlation coefficient of the age variable
H0 = "Tidak ada hubungan antara X dan Y"
H1 = "Ada hubungan antara X dan Y"
alpha = 0.05
x = health_care_df ['age']
y = health_care_df ['avg_glucose_level']
correlation_coef, p_value = stats.pearsonr(x, y)
print("Koefisien Korelasi age dan average glucose level:", correlation_coef)
print("Nilai p:", p_value)
if p_value < alpha:
  print("Hipotesis nol ditolak. Terdapat hubungan antara X dan Y")
  print(" ")
else:
  print("Tidak cukup bukti untuk menolak hipotesis nol. Tidak ada hubungan antara X dan Y")
  print(" ")

x = health_care_df ['age']
y = health_care_df ['hypertension']
correlation_coef, p_value = stats.pearsonr(x, y)
print("Koefisien Korelasi age dan hypertension : ", correlation_coef)
print("Nilai p:", p_value)
if p_value < alpha:
  print("Hipotesis nol ditolak. Terdapat hubungan antara X dan Y")
  print(" ")
else:
  print("Tidak cukup bukti untuk menolak hipotesis nol. Tidak ada hubungan antara X dan Y")
  print(" ")

x = health_care_df ['age']
y = health_care_df ['stroke']
correlation_coef, p_value = stats.pearsonr(x, y)
print("Koefisien Korelasi age dan stroke : ", correlation_coef)
print("Nilai p:", p_value)
if p_value < alpha:
  print("Hipotesis nol ditolak. Terdapat hubungan antara X dan Y")
  print(" ")
else:
  print("Tidak cukup bukti untuk menolak hipotesis nol. Tidak ada hubungan antara X dan Y")
  print(" ")
  
# test the correlation coefficient of the stroke variable
x = health_care_df ['stroke']
y = health_care_df ['hypertension']
correlation_coef, p_value = stats.pearsonr(x, y)
print("Koefisien Korelasi antara stroke dan hypertension:", correlation_coef)
print("Nilai p:", p_value)
x = health_care_df ['stroke']
y = health_care_df ['heart_disease']
correlation_coef, p_value = stats.pearsonr(x, y)
print("Koefisien Korelasi stroke dan heart disease:", correlation_coef)
print("Nilai p:", p_value)
x = health_care_df ['stroke']
y = health_care_df ['avg_glucose_level']
correlation_coef, p_value = stats.pearsonr(x, y)
print("Koefisien Korelasi stroke dan average glucose level:", correlation_coef)
print("Nilai p:", p_value)
x = health_care_df ['age']
y = health_care_df ['stroke']
correlation_coef, p_value = stats.pearsonr(x, y)
print("Koefisien Korelasi antara age dan stroke:", correlation_coef)
print("Nilai p:", p_value)