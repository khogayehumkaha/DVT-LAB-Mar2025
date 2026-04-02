import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

# Load the dataset
df = pd.read_csv('Social_Network_Ads.csv')


# --- TASK A & B: Calculations for Age and Salary ---
print("AGE")  
print("Average:",df['Age'].mean())  
print("Varience:",df['Age'].var())  
print("Median:",df['Age'].median())  
print("Quartile:",df['Age'].quantile([0.25, 0.5, 0.75]).tolist())  

print('Salary')  
print("Average:",df['EstimatedSalary'].mean())  
print("Varience:",df['EstimatedSalary'].var())  
print("Median:",df['EstimatedSalary'].median())  
print("Quartile:",df['EstimatedSalary'].quantile([0.25, 0.5, 0.75]).tolist())

# --- TASK C: Plot Histogram of Age ---
plt.hist(df['Age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Histogram of Age (Before Outlier Treatment)')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# --- TASK D: Outlier Treatment : Formula: (data - mean ) > (3 * std_dev)
abss = np.abs( df['Age'] - df['Age'].mean() ) 
dev_thresh = df['Age'].std() * 3
outlc = abss > dev_thresh
df.loc[outlc, 'Age'] = df['Age'].mean()


# Plotting the histogram again
plt.hist(df['Age'], bins=15, color='red', edgecolor='black')  
plt.title("Age With Outliers")  
plt.xlabel("Age")  
plt.ylabel("Freq")  
plt.show()

