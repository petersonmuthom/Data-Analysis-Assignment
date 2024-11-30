import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load dataset (replace 'your_dataset.csv' with your file path)
    dataset = pd.read_csv('your_dataset.csv')
    
    # Display the first few rows of the dataset
    print("\nFirst few rows of the dataset:")
    print(dataset.head())

    # Check the structure of the dataset
    print("\nDataset info:")
    print(dataset.info())

    # Check for missing values
    print("\nMissing values:")
    print(dataset.isnull().sum())

    # Clean the dataset (fill or drop missing values)
    dataset = dataset.dropna()  # Dropping rows with missing values
    print("\nDataset after cleaning:")
    print(dataset.info())

except FileNotFoundError:
    print("Error: The dataset file was not found.")
    exit()

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic Statistics:")
print(dataset.describe())

# Grouping by a categorical column (replace 'CategoryColumn' and 'NumericColumn' with actual column names)
if 'CategoryColumn' in dataset.columns and 'NumericColumn' in dataset.columns:
    grouped_data = dataset.groupby('CategoryColumn')['NumericColumn'].mean()
    print("\nMean of NumericColumn grouped by CategoryColumn:")
    print(grouped_data)
else:
    print("\nEnsure 'CategoryColumn' and 'NumericColumn' exist in your dataset for grouping.")

# Task 3: Data Visualization
# Line Chart (replace 'DateColumn' and 'NumericColumn' with actual column names)
if 'DateColumn' in dataset.columns and 'NumericColumn' in dataset.columns:
    plt.figure(figsize=(10, 6))
    dataset['DateColumn'] = pd.to_datetime(dataset['DateColumn'])
    dataset.sort_values('DateColumn', inplace=True)
    plt.plot(dataset['DateColumn'], dataset['NumericColumn'], label='Trend')
    plt.title('Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

# Bar Chart
if 'CategoryColumn' in dataset.columns and 'NumericColumn' in dataset.columns:
    plt.figure(figsize=(10, 6))
    grouped_data.plot(kind='bar', color='skyblue')
    plt.title('Average NumericColumn by CategoryColumn')
    plt.xlabel('Category')
    plt.ylabel('Average Value')
    plt.show()

# Histogram (replace 'NumericColumn' with actual column name)
if 'NumericColumn' in dataset.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(dataset['NumericColumn'], kde=True, color='purple')
    plt.title('Distribution of NumericColumn')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Scatter Plot (replace 'NumericColumn1' and 'NumericColumn2' with actual column names)
if 'NumericColumn1' in dataset.columns and 'NumericColumn2' in dataset.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=dataset['NumericColumn1'], y=dataset['NumericColumn2'], color='green')
    plt.title('Scatter Plot: NumericColumn1 vs NumericColumn2')
    plt.xlabel('NumericColumn1')
    plt.ylabel('NumericColumn2')
    plt.show()

print("\nAnalysis and visualizations are complete. Replace placeholder column names with actual names from your dataset.")
