import pandas as pd
file_path1= r"C:\Users\Apetrei\Documents\Python\applications.csv"
file_path2= r"C:\Users\Apetrei\Documents\Python\industries.csv"
applications=pd.read_csv(file_path1)
industries=pd.read_csv(file_path2)
#1. Eliminate duplicates based on the 'applicant_id' column
applications=applications.drop_duplicates(subset='applicant_id')

# 2. Fill missing values in the 'External Rating' column with zero
applications['External Rating'] = applications['External Rating'].fillna(0)

# 3. Fill missing values in the 'Education level' column with the text "Average"
applications['Education level'] = applications['Education level'].fillna("Average")
applications.head()
print(applications)
print(".......................")
merged_df = applications.merge(industries, on='Industry', how='outer')
merged_df.head()
merged_df['Evaluation'] = 0
import numpy as ny
merged_df.head()
print(merged_df.dtypes)
import matplotlib.pyplot as plt
merged_df['Applied at'] = pd.to_datetime(merged_df['Applied at'], format='mixed')
print(merged_df.dtypes)
merged_df['Evaluation'] += (merged_df['Age'].between(35, 55)) * 20
merged_df['Evaluation'] += (merged_df['Applied at'].dt.dayofweek >= 5) * 20
merged_df['Evaluation'] += (merged_df['Location'].str.contains('Kyiv')) * 10
merged_df['Evaluation'] += merged_df['Score'].clip(0, 20)
merged_df['Evaluation'] += (merged_df['External Rating'] >= 7) * 20
merged_df['Evaluation'] -= (merged_df['External Rating'] <= 2) * 20
merged_df['Evaluation'] += (merged_df['Marital status'] == 'Married') * 20
merged_df.loc[merged_df['Amount'].isna() | (merged_df['External Rating'] == 0), 'Evaluation'] = 0
merged_df['Evaluation'] = merged_df['Evaluation'].clip(0, 100)
merged_df.head()
successful_applicants = merged_df[merged_df['Evaluation'] > 0]
successful_applicants.head()
print(successful_applicants)
merged_df['Applied at'] = pd.to_datetime(merged_df['Applied at'], format='mixed', errors='coerce')
merged_df.head(20)
print(merged_df[merged_df['Applied at'].isnull()])
merged_df['Week'] = merged_df['Applied at'].dt.isocalendar().week
weekly_evaluation_mean = merged_df.groupby('Week')['Evaluation'].mean()
plt.plot(weekly_evaluation_mean.index, weekly_evaluation_mean.values, marker='*', color = 'cyan')
plt.title('Average Evaluation Points for Successful Applicants by Week')
plt.xlabel('Week of Application Submission')
plt.ylabel('Average Evaluation Points')
plt.show()