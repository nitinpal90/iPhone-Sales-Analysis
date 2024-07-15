#!/usr/bin/env python
# coding: utf-8

# # iPhone Sales Analysis

# ### Big-Data Analysis with Python

# ![Rumored-iPhone-15-Ultra-8K-video-longer-battery-life-larger-screen-bigger-price-tag-removebg-preview.png](attachment:Rumored-iPhone-15-Ultra-8K-video-longer-battery-life-larger-screen-bigger-price-tag-removebg-preview.png)

# #### This project involves analyzing sales data for Apple iPhones to identify trends and insights.

# #### The dataset was sourced from Apple's quarterly sales reports and is available on the Kaggle website for free.

# In[91]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[92]:


data = pd.read_csv("apple_products.csv")


# In[93]:


data.head(10)


# ### Task 1. Find and remove missing value in data set.

# In[94]:


print(data.isnull().sum())


# ### Task 2. Show the discripted analysis of the data set.

# In[95]:


print(data.describe())


# ### Task 3. Find the top 10 iPhones on sale in india with their rating and names.

# In[96]:


highest_Rated = data.sort_values(by = ['Star Rating'], ascending = False)
highest_Rated = data.head(10)
print(highest_Rated['Product Name'])


# ### Task 4. Find how many people have rated the best iPhones on Flipkart.

# In[97]:


iphones = highest_Rated["Product Name"].value_counts()
labels = iphones.index
counts = highest_Rated["Number Of Ratings"]
figure = px.bar(highest_Rated, x = labels, y = counts, title = "Number of the best-rated iPhone ratings")
figure.show()


# ### Task 5. Find how many people have reviews the best iPhones on Flipkart.

# In[98]:


iphones = highest_Rated["Product Name"].value_counts()
labels = iphones.index
counts = highest_Rated["Number Of Reviews"]
figure = px.bar(highest_Rated, x = labels, y = counts, title = "Number of highly-reviewed iPhone reviews")
figure.show()


# ### Task 6. Find the relationship between sale price and number of ratings with the help of graph.

# In[99]:


figure = px.scatter(data_frame = data, x = 'Number Of Ratings', y = 'Sale Price', size = 'Discount Percentage',
                   trendline = 'ols', title = 'Relationship between Sale Price and Number of Ratings.')
figure.show()


# ### Task 7. Find the Relationship between Discount Percentage and Number of Rating.

# In[100]:


figure = px.scatter(data_frame = data, x = 'Number Of Ratings', y = 'Discount Percentage', size = 'Sale Price',
                   trendline = 'ols', title = 'Relationship between Discount Percentage and Number of Rating.')
figure.show()

