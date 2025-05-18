import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
df = pd.read_csv("commute_data.csv")

# Create output folder
os.makedirs("visualizations", exist_ok=True)

# Commute time by entry station
plt.figure(figsize=(10, 6))
sns.boxplot(x="entry_station", y="commute_time_min", data=df)
plt.xticks(rotation=45)
plt.title("Commute Time Distribution by Entry Station")
plt.tight_layout()
plt.savefig("visualizations/commute_time_by_station.png")
plt.clf()

# Payment method usage
plt.figure(figsize=(6, 4))
df['payment_method'].value_counts().plot(kind='bar', color=['orange', 'green'])
plt.title("Payment Method Distribution")
plt.ylabel("Number of Commutes")
plt.savefig("visualizations/payment_method_distribution.png")
plt.clf()

# Delay vs Transfers
plt.figure(figsize=(8, 6))
sns.scatterplot(x="transfer_count", y="train_delay_min", data=df)
plt.title("Train Delay vs. Transfer Count")
plt.savefig("visualizations/delay_vs_transfers.png")
plt.clf()

# Print basic summary
print("Average Commute Time:", df['commute_time_min'].mean())
print("Most Common Entry Station:", df['entry_station'].mode()[0])
print("Most Used Payment Method:", df['payment_method'].mode()[0])
