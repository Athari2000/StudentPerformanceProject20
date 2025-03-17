# -*- coding: utf-8 -*-
"""Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PYCoNaRsg6m3xuDre0QiKP-rm0ORtN5J
"""

import pandas as pd

# Load the dataset
df = pd.read_csv('StudentPerformanceFactors.csv')

# Developing a function for descriptive statistics for a given field
def desc_stat(ds, var):


    mean = ds[var].mean()
    median = ds[var].median()
    mode = ds[var].mode()[0]
    minimum = ds[var].min()
    maximum = ds[var].max()
    data_range = maximum - minimum
    std_dev = ds[var].std()
    variance = ds[var].var()
    skew = ds[var].skew()
    kurtosis = ds[var].kurt()
    Quart = [
        ds[var].quantile(0),
        ds[var].quantile(0.25),
        ds[var].quantile(0.50),
        ds[var].quantile(0.75),
        ds[var].quantile(1),
        ds[var].quantile(0.75) - ds[var].quantile(0.25)
    ]
    count = ds[var].count()

    summary = {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Minimum": minimum,
        "Maximum": maximum,
        "Range": data_range,
        "Std Dev": std_dev,
        "Variance": variance,
        "Skewness": skew,
        "Kurtosis": kurtosis,
        "25th Percentile (Q1)": Quart[1],
        "50th Percentile (Median/Q2)": Quart[2],
        "75th Percentile (Q3)": Quart[3],
        "Inter Quartile Range (IQR)": Quart[5],
        "Count": count
    }

    # Printing the report in an organized way
    print(f"Detailed Descriptive Statistics Report for '{var}':\n")

    categories = {
        "Measures of Tendency": ["Mean", "Median", "Mode"],
        "Measures of Dispersion": ["Range", "Std Dev", "Variance", "Inter Quartile Range (IQR)"],
        "Measures of Position": ["25th Percentile (Q1)", "50th Percentile (Median/Q2)", "75th Percentile (Q3)", "Minimum", "Maximum", "Skewness", "Kurtosis"],
        "Measures of Frequency": ["Count"]
    }

    for category, measures in categories.items():
        print(category + ":")
        for measure in measures:
            print(f"{measure:<30}: {summary[measure]}")
        print()

#Random Sampling (size = 150)
random_sample = df.sample(n=150, replace=False, random_state=42)

#Applying the descriptive function to the dependent variable 'Exam_Score'
print("\n--> Using Random Sampling")
desc_stat(random_sample, 'Exam_Score')

# Systematic Sampling
systematic_sample = df.iloc[::30]

# Applying the descriptive function we created
print('\n--> Using Systematic Sampling')
desc_stat(systematic_sample, 'Exam_Score')

# Detailed Descriptive Statistics Report About the Dependent Variable 'Exam_Score'

print('\n--> Using the Whole Dataset')
desc_stat(df, 'Exam_Score')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure df is already loaded
# Convert 'Exam_Score' and independent variables to numeric (coerce errors to NaN)
numeric_columns = ['Hours_Studied', 'Attendance', 'Parental_Involvement',
                   'Access_to_Resources', 'Extracurricular_Activities',
                   'Sleep_Hours', 'Previous_Scores', 'Motivation_Level',
                   'Internet_Access', 'Tutoring_Sessions', 'Teacher_Quality',
                   'Peer_Influence', 'Exam_Score']

df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Fill missing values only for numeric columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Scatter plot settings
num_cols = 4  # Number of columns in subplot
num_vars = len(numeric_columns) - 1  # Exclude 'Exam_Score'
num_rows = (num_vars + num_cols - 1) // num_cols  # Ensures enough rows

fig, axes = plt.subplots(num_rows, num_cols, figsize=(18, 12))
axes = axes.flatten()

# Scatter plots for each independent variable vs 'Exam_Score'
for idx, column in enumerate(numeric_columns[:-1]):  # Exclude 'Exam_Score' itself
    scatter = axes[idx].scatter(df[column], df['Exam_Score'], alpha=0.5,
                                c=df[column], cmap='viridis', edgecolors='k')
    axes[idx].set_xlabel(column)  # Independent variable on X-axis
    axes[idx].set_ylabel('Exam Score')  # Dependent variable on Y-axis
    axes[idx].set_title(f'Exam Score vs {column}')
    axes[idx].grid(True)

# Hide any unused subplots
for idx in range(num_vars, len(axes)):
    fig.delaxes(axes[idx])

# Adjust layout and show the plots
plt.subplots_adjust(hspace=0.4, wspace=0.4)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Box Plot for the dependent variable 'Exam_Score'
plt.figure(figsize=(10, 4))
sns.boxplot(x=df['Exam_Score'], palette=['lightgreen'])
plt.xlabel('Exam Score')
plt.title('Distribution of Exam Scores')

# Adjusting the x-axis limits (if needed)
plt.xlim(df['Exam_Score'].min() - 5, df['Exam_Score'].max() + 5)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Histogram for the dependent variable 'Exam_Score'
plt.figure(figsize=(8, 6))
sns.histplot(df['Exam_Score'], bins=30, kde=True, color='#20B2AA')
plt.title('Distribution of Exam Scores')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')

plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('StudentPerformanceFactors.csv')

# Selecting only numeric columns
numeric_house_data = df.select_dtypes(include=[np.number])

# Compute correlation matrix
correlation = numeric_house_data.corr()

# Heat Map
# Creating a heat map to see the correlation between all variables of the dataset
plt.figure(figsize=(10,8))
sns.heatmap(correlation, annot=True, cmap='GnBu')
plt.title('Heatmap of Correlation')
plt.show()

from scipy.stats import spearmanr
import pandas as pd

# Load the dataset
df = pd.read_csv('StudentPerformanceFactors.csv')

# Spearman correlation (for the numerical variables 'Hours_Studied' & 'Exam_Score')
r, p = spearmanr(df['Hours_Studied'], df['Exam_Score'])

# Display the results
print('Spearman Correlation: r = %.3f, p = %.3f' % (r, p))

# Interpreting results
if p > 0.05:
    print('Independent categories (fail to reject H0)')
else:
    print('Dependent categories (reject H0)')

from scipy.stats import pearsonr
import pandas as pd

# Load the dataset
df = pd.read_csv('StudentPerformanceFactors.csv')

# Pearson correlation (for the numerical variables 'Hours_Studied' & 'Exam_Score')
r, p = pearsonr(df['Hours_Studied'], df['Exam_Score'])

# Display the results
print('Pearson Correlation: r = %.3f, p = %.3f' % (r, p))

# Interpreting results
if p > 0.05:
    print('Independent categories (fail to reject H0)')
else:
    print('Dependent categories (reject H0)')

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Load the dataset
df = pd.read_csv('StudentPerformanceFactors.csv')

# Creating bins for Exam Scores to categorize them (e.g., Low, Medium, High)
bin_edges = np.linspace(df['Exam_Score'].min(), df['Exam_Score'].max(), 5)  # 4 bins (Low, Medium, High, Very High)
labels = ['Low', 'Medium', 'High', 'Very High']  # Labels for bins

# Creating the Exam Score Category column
df['Exam Category'] = pd.cut(df['Exam_Score'], bins=bin_edges, labels=labels, include_lowest=True)

# Creating the contingency table (example: Exam Category vs Gender)
contingency_data = pd.crosstab(df['Gender'], df['Exam Category'], margins=False)
print(contingency_data.head(5))

# Performing Chi-square test
r, p, dof, expected = chi2_contingency(contingency_data)
print('\nChi-square value: %.3f, p = %.3f' % (r, p))

# Interpreting results
if p > 0.05:
    print('Independent categories (fail to reject H0)')
else:
    print('Dependent categories (reject H0)')

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Load the dataset
df = pd.read_csv('StudentPerformanceFactors.csv')

# Creating bins for Exam Scores to categorize them for chi-square testing
bin_edges = np.linspace(df['Exam_Score'].min(), df['Exam_Score'].max(), 31)
labels = [f'Bin {i}' for i in range(1, 31)]  # Labels for each bin

# Creating the Exam Score categorical column
df['Exam Score Category'] = pd.cut(df['Exam_Score'], bins=bin_edges, labels=labels, include_lowest=True)

# Creating the contingency table ( Exam Score Category vs Gender)
contingency_data = pd.crosstab(df['Gender'], df['Exam Score Category'], margins=False)
print(contingency_data.head(5))

# Performing Chi-square test for contingency table
r, p, dof, expected = chi2_contingency(contingency_data)
print('\nChi-square value: %.3f, p = %.3f' % (r, p))

# Interpreting results
if p > 0.05:
    print('Independent categories (fail to reject H0)')
else:
    print('Dependent categories (reject H0)')