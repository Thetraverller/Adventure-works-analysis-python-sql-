import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np

# Define the file path for the CSV file
file_path = r'C:\Users\mtanz\Desktop\DA projects\Group project 1\q6_query.csv'

# Specify the column names
column_names = ['Name', 'AnnualRevenue', 'SquareFeet', 'NumberEmployees']

# Read the CSV file into a DataFrame with the specified column names
df = pd.read_csv(file_path, names=column_names)

# Convert revenue column to integers
df['AnnualRevenue'] = df['AnnualRevenue'].astype(int)

# Define the unique revenue categories in ascending order
unique_revenues = [30000, 80000, 100000, 150000, 300000]

correlation_values = []

# Calculate correlation and create scatter plot for each revenue category
for revenue in unique_revenues:
    # Filter the dataframe for the specific revenue category
    filtered_df = df[df['AnnualRevenue'] == revenue]

    # Calculate correlation coefficient between size and number of employees
    correlation, _ = pearsonr(filtered_df['SquareFeet'], filtered_df['NumberEmployees'])
    correlation = round(correlation, 2)

    correlation_values.append(correlation)

    # Plot size (square feet) against number of employees
    plt.scatter(filtered_df['SquareFeet'], filtered_df['NumberEmployees'], label=f"Revenue: {revenue}, Correlation: {correlation}")

# Calculate average correlation
average_correlation = np.mean(correlation_values)
average_correlation = round(average_correlation, 2)

# Set plot labels and title
plt.xlabel('Size (Square Feet)')
plt.ylabel('Number of Employees')
plt.title('Correlation between Size and Number of Employees for Unique Revenue Categories')

# Add the legend
plt.legend(title='Legend', loc='center left', bbox_to_anchor=(1, 0.5))

# Add the average correlation as text
plt.text(83000, 27, f'Average Correlation: {average_correlation}', ha='right')

# Display the plot
plt.show()
