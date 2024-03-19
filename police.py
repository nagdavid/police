import pandas as pd

df = pd.read_csv("Police_data.csv")

#Q. 1) Instruction ( For Data Cleaning ) - Remove the column that only contains missing values.

df.dropna(axis=1,how='all',inplace=True)
print(df)

#Q. 2) Question ( Based on Filtering + Value Counts ) - For Speeding , were Men or Women stopped more often ? 
import pandas as pd
speeding_df = df[df['violation_raw'] == 'Speeding']

gender_counts = speeding_df['driver_gender'].value_counts()

print("Number of speeding violations by gender:")
print(gender_counts)

#Q. 3) Question ( Groupby ) - Does gender affect who gets searched during a stop ?Question ( mapping + data-type casting )

search_stats = df.groupby('driver_gender')['search_conducted'].value_counts(normalize=True) * 100

print("Percentage of searches conducted by gender:")
print(search_stats)

#Q. 4) Question ( mapping + data-type casting ) - What is the mean stop_duration ?
duration_mapping = {'0-15 Min': 7.5, '16-30 Min': 23, '30+ Min': 45}
df['stop_duration'] = df['stop_duration'].map(duration_mapping)

df['stop_duration'] = pd.to_numeric(df['stop_duration'])

mean_stop_duration = df['stop_duration'].mean()

print("Mean stop duration:", mean_stop_duration)

#Q. 5) Question ( Groupby , Describe ) - Compare the age distributions for each violation

age_stats_by_violation = df.groupby('violation')['driver_age'].describe()

print("Age distribution summary statistics for each violation:")
print(age_stats_by_violation)







