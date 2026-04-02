# 0. Import modules / packages
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv('Position_Salaries.csv')


# a. Display first and last few rows
print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

# b. Display selected columns: Position and Salary
print("\n Position and Salary  Data :")
print(df[['Position', 'Salary']])

# c. Display the rows with Salary > 90,000
print("\nRows with Salary > 90,000:")
print(df[df['Salary'] > 90000])

# d. Create a column TDS with TDS = 10% of Salary
df['TDS'] = 0.10 * df['Salary']
print("\nDataset with TDS Column:")
print(df.head())

# e. Sort the dataset based on Position
#sorted_df = df.sort_values(by='Position',ascending=False)
sorted_df = df.sort_values(by='Position')
print("\nDataset sorted by Position:")
print(sorted_df)

# f. Group the dataset by Level and calculate the mean salary
mean_salary = df.groupby('Level')['Salary'].mean()
print("\nMean Salary by Level:")
print(mean_salary)

# g. Plot the graph: Level vs Salary
plt.plot(df['Level'], df['Salary'], marker='o', color='green')
plt.title('Level vs Salary')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.grid(True)
plt.show()


