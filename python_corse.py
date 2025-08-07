import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("homelessness.csv")
print(df.head())
print(df.columns)
#Total homelessness by state.
state_totals = df.groupby('state')[['individuals', 'family_members']].sum()
print("Total homeless by state:")
print(state_totals.sort_values('individuals', ascending=False).head())

# Total homeless individuals by region
region_totals = df.groupby('region')[['individuals', 'family_members']].sum()
print("\nTotal homeless by region:")
print(region_totals.sort_values('individuals', ascending=False))

# Plot total homeless individuals by region
region_totals['individuals'].plot(kind='bar', title='Total Homeless Individuals by Region')
plt.ylabel('Number of Individuals')
plt.show()

# Calculate homelessness rate per 10,000 people in each state
df['total_homeless'] = df['individuals'] + df['family_members']
df['homeless_rate_per_10k'] = (df['total_homeless'] / df['state_pop']) * 10000

# Show top 5 states with highest homelessness rate per 10,000 people
print("\nTop 5 states by homelessness rate per 10,000 people:")
print(df[['state', 'homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=False).head())

# Plot homelessness rate per 10,000 people by state (top 10 states)
top_states = df[['state', 'homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_states['state'], top_states['homeless_rate_per_10k'], color='skyblue')
plt.xlabel('Homelessness Rate per 10,000 People')
plt.title('Top 10 States by Homelessness Rate per 10,000 People')
plt.gca().invert_yaxis()  # Highest rate at the top
plt.show()

# Calculate the proportion of family homelessness in each state
df['family_homeless_pct'] = (df['family_members'] / df['total_homeless']) * 100

# Show top 5 states where family homelessness is a larger proportion of the total
print("\nTop 5 states by proportion of family homelessness:")
print(df[['state', 'family_homeless_pct']].sort_values('family_homeless_pct', ascending=False).head())

# Optional: Plot the top 10 states by family homelessness proportion
top_family_states = df[['state', 'family_homeless_pct']].sort_values('family_homeless_pct', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_family_states['state'], top_family_states['family_homeless_pct'], color='orange')
plt.xlabel('Family Homelessness (% of Total)')
plt.title('Top 10 States by Family Homelessness Proportion')
plt.gca().invert_yaxis()
plt.show()

# Calculate total homeless and population by region
region_stats = df.groupby('region').agg({
    'individuals': 'sum',
    'family_members': 'sum',
    'state_pop': 'sum'
})

region_stats['total_homeless'] = region_stats['individuals'] + region_stats['family_members']
region_stats['homeless_rate_per_10k'] = (region_stats['total_homeless'] / region_stats['state_pop']) * 10000

# Show regions with highest and lowest homelessness rates
print("\nHomelessness rate per 10,000 people by region:")
print(region_stats[['homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=False))

# Plot homelessness rate per 10,000 people by region
plt.figure(figsize=(8, 5))
region_stats['homeless_rate_per_10k'].sort_values(ascending=False).plot(kind='bar', color='purple')
plt.ylabel('Homelessness Rate per 10,000 People')
plt.title('Homelessness Rate per 10,000 People by Region')
plt.show()

# Top 5 states with highest homelessness rates
print("\nTop 5 states by homelessness rate per 10,000 people:")
print(df[['state', 'homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=False).head(5))

# Bottom 5 states with lowest homelessness rates
print("\nBottom 5 states by homelessness rate per 10,000 people:")
print(df[['state', 'homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=True).head(5))
# ...existing code...

# Plot top 5 states by homelessness rate per 10,000 people
top5_states = df[['state', 'homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=False).head(5)
plt.figure(figsize=(8, 4))
plt.barh(top5_states['state'], top5_states['homeless_rate_per_10k'], color='red')
plt.xlabel('Homelessness Rate per 10,000 People')
plt.title('Top 5 States by Homelessness Rate per 10,000 People')
plt.gca().invert_yaxis()
plt.show()

# Plot bottom 5 states by homelessness rate per 10,000 people
bottom5_states = df[['state', 'homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=True).head(5)
plt.figure(figsize=(8, 4))
plt.barh(bottom5_states['state'], bottom5_states['homeless_rate_per_10k'], color='green')
plt.xlabel('Homelessness Rate per 10,000 People')
plt.title('Bottom 5 States by Homelessness Rate per 10,000 People')
plt.gca().invert_yaxis()
plt.show()

# Bar chart: Total homeless individuals by region
region_totals = df.groupby('region')[['individuals', 'family_members']].sum()
region_totals['individuals'].plot(kind='bar', title='Total Homeless Individuals by Region', color='steelblue')
plt.ylabel('Number of Individuals')
plt.xlabel('Region')
plt.tight_layout()
plt.show()

# Bar chart: Top 10 states by total homeless individuals
state_totals = df.groupby('state')[['individuals', 'family_members']].sum()
top10_states = state_totals.sort_values('individuals', ascending=False).head(10)
top10_states['individuals'].plot(kind='bar', title='Top 10 States by Total Homeless Individuals', color='teal')
plt.ylabel('Number of Individuals')
plt.xlabel('State')
plt.tight_layout()
plt.show()