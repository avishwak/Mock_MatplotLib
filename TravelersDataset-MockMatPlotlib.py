import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('travel.csv')
df
# the datastet contains information about travelers: Month 	Destination 	Travelers 	Revenue

# 1. Line Plot: Create a line plot using Matplotlib that illustrates the trend of both traveler count and revenue 
# over the past year. The x-axis should represent the months, while the y-axis should represent the traveler count 
# and revenue, respectively. The line plot should display two lines, one for traveler count and another for revenue

# the scales of travelers and revenue differ vastly so i plotted in log scale
dl = df.groupby('Month')[['Travelers', 'Revenue']].sum().reset_index()
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
dl['Month'] = pd.Categorical(dl['Month'], categories=month_order, ordered=True)
dl.sort_values('Month', inplace=True)
plt.plot(dl.Month, dl.Travelers, label = '# Travelers')
plt.plot(dl.Month, dl.Revenue/100, label = 'Revenue *100')
plt.xlabel('Month')
plt.ylabel('revenue and # travelers')
plt.legend()
plt.show()

# another approach I used was to normalise the data to a range of 0 to 1
# this way we can compare the two variables on the same scale
# Normalization formula: (x - min) / (max - min)
dl_norm = (dl[['Travelers', 'Revenue']] - dl[['Travelers', 'Revenue']].min()) / \
                  (dl[['Travelers', 'Revenue']].max() - dl[['Travelers', 'Revenue']].min())
dl_norm['Month'] = dl['Month'] # adding the Month column back to the normalized DataFrame
dl_norm
plt.plot(dl_norm.Month, dl_norm.Travelers, label = 'Travelers Count (Normalized)', marker = 'o', markersize = 8)
plt.plot(dl_norm.Month, dl_norm.Revenue, label = 'Revenue (Normalized)', marker = 's', markersize = 3, linestyle='--')
plt.xlabel('Month')
plt.ylabel('Value Normalised to 1')
plt.title('Monthly Trend of Travelers and Revenue (Normalized to 1)')
plt.legend()
plt.show()


# 2. Pie Chart: Generate a pie chart using Matplotlib to display the distribution of traveler count among the top 
# five destinations for the entire year. Each slice of the pie should represent a destination, and its size should 
# correspond to the proportion of travelers visiting that particular destination.

dp = df.groupby('Destination')[['Travelers']].sum().sort_values('Travelers', ascending=False).reset_index()
dp = dp.head(5)
plt.pie(dp.Travelers, labels=dp.Destination, autopct='%1.1f%%')
plt.title('Traveler Distribution Among Top 5 Destinations')
plt.show()

# 3. Scatter Plot: Create a scatter plot using Matplotlib that demonstrates the relationship between the number of 
# travelers and the revenue generated for each month. Each data point on the scatter plot should represent a month, 
# with the x-coordinate representing the traveler count and the y-coordinate representing the revenue generated.


# I am going to use the already generate dataframe dl for this part

x = dl.Travelers
y = dl.Revenue
plt.scatter(x, y)
for (m, xi, yi) in zip(dl.Month, x,y):
    plt.annotate(f'{m}', (xi, yi))
plt.xlabel('Travelers')
plt.ylabel('Revenue')
plt.title('Travelers Vs Revenue for Each Month')
plt.show()