import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
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
plt.savefig('charts/homeless_individuals_by_region.png', bbox_inches='tight')
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
plt.savefig('charts/homelessness_rate_per_10,000_people_by_state.png', bbox_inches='tight')
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
plt.savefig('charts/top_10_states_by_family_homelessness_proportion.png', bbox_inches='tight')
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
plt.savefig('charts/homelessness_per_region.png', bbox_inches='tight')
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
plt.savefig('charts/5_states_by_homelessness_rate_per_10,000_people.png', bbox_inches='tight')
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
plt.savefig('charts/homeless_individuals_by_region.png', bbox_inches='tight')
plt.show()

# Bar chart: Top 10 states by total homeless individuals
state_totals = df.groupby('state')[['individuals', 'family_members']].sum()
top10_states = state_totals.sort_values('individuals', ascending=False).head(10)
top10_states['individuals'].plot(kind='bar', title='Top 10 States by Total Homeless Individuals', color='teal')
plt.ylabel('Number of Individuals')
plt.xlabel('State')
plt.tight_layout()
plt.savefig('charts/Top_10_states_by_total_homeless_individuals.png', bbox_inches='tight')
plt.show()

# Data preparation
df['total_homeless'] = df['individuals'] + df['family_members']
df['homeless_rate_per_10k'] = (df['total_homeless'] / df['state_pop']) * 10000
df['family_homeless_pct'] = (df['family_members'] / df['total_homeless']) * 100

region_totals = df.groupby('region')[['individuals', 'family_members']].sum()
state_totals = df.groupby('state')[['individuals', 'family_members']].sum()
top10_states = state_totals.sort_values('individuals', ascending=False).head(10)

region_stats = df.groupby('region').agg({
    'individuals': 'sum',
    'family_members': 'sum',
    'state_pop': 'sum'
})
region_stats['total_homeless'] = region_stats['individuals'] + region_stats['family_members']
region_stats['homeless_rate_per_10k'] = (region_stats['total_homeless'] / region_stats['state_pop']) * 10000

# Streamlit dashboard
st.title("US Homelessness Data Dashboard")

st.header("Raw Data")
if st.checkbox("Show raw data"):
    st.write(df.head())

st.header("Total Homelessness by State")
st.dataframe(state_totals.sort_values('individuals', ascending=False).head(10))

st.header("Total Homelessness by Region")
st.dataframe(region_totals.sort_values('individuals', ascending=False))

st.header("Top 10 States by Total Homeless Individuals")
fig1, ax1 = plt.subplots()
top10_states['individuals'].plot(kind='bar', color='teal', ax=ax1)
plt.ylabel('Number of Individuals')
plt.xlabel('State')
plt.title('Top 10 States by Total Homeless Individuals')
st.pyplot(fig1)

st.header("Total Homeless Individuals by Region")
fig2, ax2 = plt.subplots()
region_totals['individuals'].plot(kind='bar', color='steelblue', ax=ax2)
plt.ylabel('Number of Individuals')
plt.xlabel('Region')
plt.title('Total Homeless Individuals by Region')
st.pyplot(fig2)

st.header("Top 10 States by Homelessness Rate per 10,000 People")
top_states = df[['state', 'homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=False).head(10)
fig3, ax3 = plt.subplots()
ax3.barh(top_states['state'], top_states['homeless_rate_per_10k'], color='skyblue')
ax3.set_xlabel('Homelessness Rate per 10,000 People')
ax3.set_title('Top 10 States by Homelessness Rate per 10,000 People')
ax3.invert_yaxis()
st.pyplot(fig3)

st.header("Top 10 States by Family Homelessness Proportion")
top_family_states = df[['state', 'family_homeless_pct']].sort_values('family_homeless_pct', ascending=False).head(10)
fig4, ax4 = plt.subplots()
ax4.barh(top_family_states['state'], top_family_states['family_homeless_pct'], color='orange')
ax4.set_xlabel('Family Homelessness (% of Total)')
ax4.set_title('Top 10 States by Family Homelessness Proportion')
ax4.invert_yaxis()
st.pyplot(fig4)

st.header("Homelessness Rate per 10,000 People by Region")
fig5, ax5 = plt.subplots()
region_stats['homeless_rate_per_10k'].sort_values(ascending=False).plot(kind='bar', color='purple', ax=ax5)
plt.ylabel('Homelessness Rate per 10,000 People')
plt.title('Homelessness Rate per 10,000 People by Region')
st.pyplot(fig5)

st.header("Top & Bottom 5 States by Homelessness Rate per 10,000 People")
top5_states = df[['state', 'homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=False).head(5)
bottom5_states = df[['state', 'homeless_rate_per_10k']].sort_values('homeless_rate_per_10k', ascending=True).head(5)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Top 5 States")
    fig6, ax6 = plt.subplots()
    ax6.barh(top5_states['state'], top5_states['homeless_rate_per_10k'], color='red')
    ax6.set_xlabel('Homelessness Rate per 10,000 People')
    ax6.set_title('Top 5 States')
    ax6.invert_yaxis()
    st.pyplot(fig6)
with col2:
    st.subheader("Bottom 5 States")
    fig7, ax7 = plt.subplots()
    ax7.barh(bottom5_states['state'], bottom5_states['homeless_rate_per_10k'], color='green')
    ax7.set_xlabel('Homelessness Rate per 10,000 People')
    ax7.set_title('Bottom 5 States')
    ax7.invert_yaxis()
    st.pyplot(fig7)