import pandas as pd

df = pd.read_csv('Health.csv')

median_calories = df['Calories'].median()
df['Calories'].fillna(median_calories, inplace=True)


num_participants = df.shape[0]


min_calories = df['Calories'].min()


corr_pulse_calories = df['Duration'].corr(df['Calories'])

mean_calories = df['Calories'].mean()

percentile_75_maxpulse = df['Maxpulse'].quantile(0.75)


print(f"Number of people who participated: {num_participants}")
print(f"Minimum value of 'Calories': {min_calories}")
print(f"Coefficient correlation between 'Pulse' and 'Calories': {corr_pulse_calories}")
print(f"Percentile 75 of 'Maxpulse': {percentile_75_maxpulse}")
print(f"Mean value of the pulse duration:{mean_calories}")


