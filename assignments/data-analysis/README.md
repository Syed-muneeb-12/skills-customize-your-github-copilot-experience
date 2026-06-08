# 📘 Assignment: Data Analysis

## 🎯 Objective

Learn basic data analysis with Python: load a CSV, explore its structure, compute summary statistics, and create visualizations to surface insights.

## 📝 Tasks

### 🛠️	Data Loading and Exploration

#### Description
Load the provided CSV dataset and perform exploratory data analysis to understand the table structure and numeric distributions.

#### Requirements
Completed work should:

- Implement a script or functions that load `data.csv` (use `pandas` or the `csv` module).
- Display the first 5 rows of the dataset using a `head()`-style output.
- Compute and show summary statistics for numeric columns (count, mean, median, std).

Example (pseudocode):

```python
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
print(df.describe())
```

### 🛠️	Data Visualization and Insights

#### Description
Create visualizations to illustrate distributions and relationships, and write a short summary of the most important findings.

#### Requirements
Completed work should:

- Produce at least two different plot types (for example: histogram, scatter plot, boxplot) and save them as image files (PNG or JPG).
- Include brief captions or a short report (2–4 sentences) describing at least two insights or trends discovered from the plots.
- Ensure plots include axis labels and titles.

Example (pseudocode):

```python
import matplotlib.pyplot as plt
df['column'].hist()
plt.title('Distribution of column')
plt.xlabel('value')
plt.ylabel('frequency')
plt.savefig('histogram.png')
```
