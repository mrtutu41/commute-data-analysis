import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
csv_path = os.path.join(os.path.dirname(__file__), 'commute_data.csv')
df = pd.read_csv(csv_path)

# Show first few rows
print(df.head())

# Summary stats
print("\nSummary statistics:")
print(df.describe())

# Commute time distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['commute_time_min'], bins=20, kde=True, color='skyblue')
plt.title("Distribution of Commute Times (minutes)")
plt.xlabel("Commute Time (min)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Delay frequency
plt.figure(figsize=(6, 4))
sns.countplot(x='train_delay_min', data=df, palette='Set2')
plt.title("Train Delay Frequency")
plt.xlabel("Delay (minutes)")
plt.ylabel("Number of Trips")
plt.tight_layout()
plt.show()
