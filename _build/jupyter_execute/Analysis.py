#!/usr/bin/env python
# coding: utf-8

# # Analysis of the data

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


data = pd.read_csv("CollegeRankingsData.csv")
data.head()


# In[3]:


fig = px.histogram(data, x="PercAccepted", title="Distribution of Accepted Applicants").update_layout(xaxis_tickformat=".2%")
fig.show()


# This distribution shows that colleges tend to accept most applicants.

# In[4]:


fig = px.scatter_3d(data, x = "OutStateTuition", y = "RoomBoardCosts",
                    z = "Expenditure", color="Type", width=800, height=700)
fig.show()


# 3D scatter plots are always cool to look at, and with Jupyter Book you can perform your analysis and share it with the world! This particular scatter plot shows us there may be some relationship between `OutStateTuition` and `Expenditure`.

# In[5]:


fig = px.scatter(data, x = "OutStateTuition", y = "Expenditure", color="Type",
                 trendline="ols", trendline_scope="overall", trendline_color_override="black",
                 width=800, height=700)
fig.show()


# Here we fit a linear regresssion to these variables, and we are able to obtain the regression statistics from it as well. They are shown below.

# In[6]:


results = px.get_trendline_results(fig)
results.px_fit_results.iloc[0].summary()


# The R-squared is not very high at only 0.439, but both coefficients have p-values way below 5% which indicates the linear relationship is statistically significant.

# In[7]:


schoolsPerState = data.groupby("State").size().reset_index(name='counts').sort_values("counts",ascending=False)

fig = px.bar(schoolsPerState, y='counts', x='State', color="State",
             title='Number of universities per State',
             width=900, height=800).update_layout(showlegend=False)
fig.show()


# Here is a pretty chart displaying the number of colleges in each state.
