import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1,2)
fig.suptitle('Plotting with Seaborn')
#index_col = 0 since we treat the first columns as the index
df = pd.read_csv('data.csv', index_col=0, encoding='unicode-escape')
df.head()

### Scatter plots
#Regression line is shown by default(line that best fits the data) => correlation between the 2 axes
# fit_reg=False => disables the regression line
sns.lmplot(ax = axes[0], x='Attack', y='Defense', data=df, fit_reg=False, hue='Stage')
fit_reg=False

plt.show()

### Box plots
df_copy = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
print(df_copy)
sns.boxplot(ax = axes[1], data=df_copy)
plt.show()

#Line shown is a default regression line (line that best fits the data) => correlation between the 2 axes

