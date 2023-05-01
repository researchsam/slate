#!/usr/bin/env python
# coding: utf-8

# In[106]:


import pandas as pd
import numpy as np
import math


# Read streamflow data from a CSV file
flow = pd.read_excel('../data/sac_county_water_data.xlsx')

concentration = pd.read_excel('../data/concentration.xlsx')

precipitation = pd.read_csv('../data/Precipitation.csv')

n_surplus = pd.read_excel('../data/surplus.xlsx')


# In[59]:


# checking to see if data loaded correctly

n_surplus.head(5)


# In[47]:


flow = flow.rename(columns={"Date": "date"})

concentration = concentration.rename(columns={"Date": "date"})

precipitation = precipitation.rename(columns={"DATE": "date"})

concentration.columns


# In[21]:


# Calculate the correlation between streamflow and concentration
correlation = np.corrcoef(flow["streamflow"], concentration["nitrate"])[0, 1]

print("The correlation coefficient between streamflow and concentration is", correlation)


# ## This is because of the missing data in the concentration data, as well as the mismatch in the dates between the 2 datasets, so we correct these by dropping missing columns as well as matching common dates

# In[61]:


concentration = concentration.dropna()

# Find the intersection of the dates between the two DataFrames
common_dates = flow.index.intersection(concentration.index)

# Filter the streamflow and concentration DataFrames to only include the common dates
flow = flow.loc[common_dates]
concentration = concentration.loc[common_dates]

correlation = np.corrcoef(flow["streamflow"], concentration["nitrate"])[0, 1]

print("The correlation coefficient between streamflow and concentration is", correlation)


# In[34]:


plt.scatter(flow["streamflow"], concentration["nitrate"])
plt.xlabel("Streamflow")
plt.ylabel("Concentration")
plt.title("Scatter Plot of Streamflow vs. Concentration")
plt.show()


# In[37]:


# Calculate the regression line for streamflow vs. concentration
slope, intercept = np.polyfit(flow["streamflow"], concentration["nitrate"], 1)

# Calculate the coefficient of determination (R^2)
R2 = np.corrcoef(flow["streamflow"], concentration["nitrate"])[0, 1]**2
R2


# In[54]:


intercept


# In[57]:


nsurplus_mean


# In[95]:


from sklearn.cluster import KMeans

# Create a NumPy array of the concentration data
concentration_array = concentration["nitrate"].values
concentration_array = concentration_array.reshape(-1, 1)

# Create a KMeans model with two clusters
kmeans = KMeans(n_clusters=2, random_state=42)

# Fit the KMeans model to the concentration data
kmeans.fit(concentration_array)

# Predict the cluster labels for the concentration data
cluster_labels = kmeans.predict(concentration_array)

# Create a new DataFrame with the concentration data, the cluster labels, and a binary label indicating whether the concentration is high or low
concentration_with_labels = concentration.assign(
    Cluster=cluster_labels,
    Label=(concentration_array > 10).astype(int)
)

# Print the distribution of the labels
print(concentration_with_labels["Label"].value_counts())


# In[96]:


# Create a new column in the DataFrame named "Label"
#concentration_with_labels["Label"] = (concentration_array > 10).astype(int)

# Replace all values in the "Label" column that are equal to 0 with "low"
concentration_with_labels["Label"] = concentration_with_labels_df["Label"].replace(0, "low")

# Replace all values in the "Label" column that are equal to 1 with "high"
concentration_with_labels["Label"] = concentration_with_labels_df["Label"].replace(1, "high")

# Print the first few rows of the DataFrame
print(concentration_with_labels.tail(5))


# In[108]:


# Create a figure and axes
fig, ax = plt.subplots()

# Plot the concentration data
ax.scatter(concentration_array, concentration_with_labels_df["Label"], c=["red" if label == "high" else "blue" for label in concentration_with_labels["Label"]])

# Add a legend
ax.legend(["Low", "High"])

# Set the title
plt.title("clustering of concentration data")

# Show the plot
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[64]:


precipitation.tail(5)


# In[65]:


flow = flow.rename(columns={"Date": "date"})

precipitation = precipitation.rename(columns={"DATE": "date"})

flow.columns


# In[107]:


precipitation.head(5)


# In[100]:


precipitation = precipitation.dropna()


# In[101]:


flow = flow.loc['2016-01-01':'2016-12-30']


# In[104]:


precipittion = precipitation.loc['2016-01-01':'2016-12-30'] 


# In[103]:


corr = precipitation['PRCP'].corr(flow['streamflow'])

corr


# In[ ]:




