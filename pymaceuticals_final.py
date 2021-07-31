#!/usr/bin/env python
# coding: utf-8

# ## Observations and Insights 

# 

# In[98]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np
# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)


# Combine the data into a single dataset
study_data_complete = pd.merge(study_results,
                              mouse_metadata, how="left",on=["Mouse ID", "Mouse ID"])


# Display the data table for preview
study_data_complete.head()


# In[ ]:





# In[99]:


# Checking the number of mice.
mice_count = study_data_complete['Mouse ID'].value_counts()
len(mice_count)


# In[100]:


# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
duplicate_ID_Timepoint = study_data_complete.loc[study_data_complete.duplicated(subset=['Mouse ID','Timepoint']),'Mouse ID'].unique()


# In[101]:


# Optional: Get all the data for the duplicate mouse ID. 
duplicate_mice =pd.DataFrame(duplicate_ID_Timepoint)
duplicate_mice


# In[102]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID.
clean_study_df = study_data_complete[study_data_complete['Mouse ID'].isin(duplicate_ID_Timepoint)==False]                                     


# In[103]:


# Checking the number of mice in the clean DataFrame.
clean_study_mice = clean_study_df['Mouse ID'].value_counts()
clean_mice_count = len(clean_study_mice)
clean_mice_count


# ## Summary Statistics

# In[104]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen
# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 
# Assemble the resulting series into a single summary dataframe.


mean_regimen_tumor = clean_study_df.groupby('Drug Regimen').mean() ['Tumor Volume (mm3)']
median_regimen_tumor = clean_study_df.groupby('Drug Regimen').median() ['Tumor Volume (mm3)']
var_regimen_tumor = clean_study_df.groupby('Drug Regimen').var() ['Tumor Volume (mm3)']
std_regimen_tumor = clean_study_df.groupby('Drug Regimen').std() ['Tumor Volume (mm3)']
sem__regimen_tumor = clean_study_df.groupby('Drug Regimen').sem() ['Tumor Volume (mm3)']


#Summary stats table
drug_regiment_table = pd.DataFrame({"Mean": mean_regimen_tumor, "Median": median_regimen_tumor, 
                                    "Variance": var_regimen_tumor, "Standard Deviation": std_regimen_tumor, 
                                    "SEM": sem__regimen_tumor})
drug_regiment_table


# In[105]:


# Using the aggregation method, produce the same summary statistics in a single line

#Regimen agg method (method - Using the aggregation method, produce the same summary statistics in a single line)
aggMethod = clean_study_df.groupby('Drug Regimen')
aggMethod.agg(
    {
        "Tumor Volume (mm3)": ["mean", "median", "var", "std", "sem"]
    }
)



# ## Bar and Pie Charts

# In[106]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using pandas.
drug_regiment_total = clean_study_df.groupby('Drug Regimen').count() ['Tumor Volume (mm3)']
drug_regiment_total_df = pd.DataFrame(drug_regiment_total)
drug_regiment_total_df.plot(kind="bar",legend=False)

plt.ylabel("Total Number of Measurements Taken")
plt.show()
plt.tight_layout()


# In[107]:


# Generate a bar plot showing the total number of measurements taken on each drug regimen using pyplot.

x_axis = np.arange(len(drug_regiment_total_df))
plt.bar(x_axis,drug_regiment_total, alpha=0.8)

tick_locations = [value for value in x_axis]

plt.xticks(xtick_locations, ['Capomulin', 'Ceftamin', 'Infubinol', 'Ketapril', 'Naftisol', 'Placebo', 'Propriva', 'Ramicane', 'Stelasyn', 'Zoniferol'],  rotation='vertical')



plt.xlabel("Drug Regimen")
plt.ylabel("Total Number of Measurements Taken")
plt.show()
plt.tight_layout()


# In[130]:


#Mice sex data
mouse_sex_data = mouse_metadata.groupby("Sex").count()
mouse_sex_data_totals = mouse_sex_data["Mouse ID"]
mouse_sex_data_totals


# In[137]:


#mice sex percentages
mouse_sex_percentages = (100* (mouse_sex_data_totals/mouse_sex_data_totals.sum())).astype(float)
mouse_sex_percentages


# In[146]:


# Generate a pie plot showing the distribution of female versus male mice using pandas
mice_sex_chart = mouse_sex_percentages.plot(kind="pie", title="Mice Sex")



plt.show()
plt.tight_layout()


# In[143]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot
labels = ['Female', 'Male']
sizes = mouse_sex_percentages
colors = ['red', 'teal']
explode = (0.1,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)


# ## Quartiles, Outliers and Boxplots

# In[183]:


# Calculate the final tumor volume of each mouse across four of the treatment regimens:  

#combine and rename columns for max timepoint -treatments - for rename (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html)
treatment_last_timepoint_df = pd.DataFrame(clean_study_df.groupby('Mouse ID')['Timepoint'].max().sort_values()).reset_index().rename(columns={'Timepoint': 'max_timepoint'})

merged_treatment_df = pd.merge(clean_study_df, treatment_last_timepoint_df, on="Mouse ID")
merged_treatment_df.head()


# In[185]:


# Put treatments into a list for for loop (and later for plot labels)
treatments = ['Capomulin', 'Ramicane', 'Infubinol', 'Ceftamin']

# Create empty list to fill with tumor vol data (for plotting)
tumor_vol_data = []

# Calculate the IQR and quantitatively determine if there are any potential outliers. 
for treatment in treatments:
    
    #Locate the rows which contain mice on each drug and get the tumor volumes 
    
    treatments_df = merged_treatment_df.loc[merged_treatment_df['Drug Regimen'] == treatment]
    
    #add subset 
    
    final_volume_df = treatments_df.loc[treatments_df['Timepoint'] == treatments_df['max_timepoint']]
    
    #create a series that lists all final tumor values
    values = final_volume_df['Tumor Volume (mm3)']
    
    tumor_vol_data.append(values)
    

    #Determine outliers using upper and lower bounds
    
    quartiles = values.quantile([.25, .5, .75])
    lowerq = quartiles[.25]
    upperq = quartiles[.75]
    iqr = upperq - lowerq
    
    print(f'IQR for {treatment}: {iqr}')
    
    #find upper and lower bounds to identify outliers
    lower_bound = lowerq - (1.5*iqr)
    upper_bound = upperq + (1.5*iqr)
    
    print(f'Lower Bound for {treatment}: {lower_bound}')
    print(f'Upper Bound for {treatment}: {upper_bound}')
    
    #Check for ouliers
    outliers_count = (values.loc[(final_volume_df['Tumor Volume (mm3)'] >= upper_bound) |
                                (final_volume_df['Tumor Volume (mm3)'] <= lower_bound)]).count()
    
    print(f'Number of {treatment} outliers: {outliers_count}')
    


# In[199]:


# Generate a box plot of the final tumor volume of each mouse across four regimens of interest


plt.boxplot(tumor_vol_data)


plt.title('Final Tumor Volume by Regimens')
plt.ylabel('Final Tumor Volume (mm3)')
plt.xticks([1, 2, 3, 4], ['Capomulin', 'Ramicane', 'Infubinol', 'Ceftamin'])

plt.show()


# ## Line and Scatter Plots

# In[201]:


# Generate a line plot of tumor volume vs. time point for a mouse treated with Capomulin

#data for a specific mouse
specific_mouse  = merged_treatment_df.loc[merged_treatment_df['Mouse ID']== 'm601']
specific_mouse
#plot data
plt.plot(specific_mouse['Timepoint'],specific_mouse['Tumor Volume (mm3)'])
plt.xlabel("Days")
plt.ylabel("Tumor Volume (mm3)")
plt.title("Capomulin treatment m601")


plt.show()


# In[224]:


# Generate a scatter plot of average tumor volume vs. mouse weight for the Capomulin regimen

#Data for the scatter plot
Capomulin_df = merged_treatment_df.loc[merged_treatment_df['Drug Regimen'] == 'Capomulin']
Capomulin_df

avg_Capomulin_vol = pd.DataFrame(Capomulin_df.groupby('Mouse ID')['Tumor Volume (mm3)'].mean()).reset_index().rename(columns={'Tumor Volume (mm3)': 'avg_tumor_vol'})

avg_Capomulin_vol

avg_Capomulin_vol = pd.merge(Capomulin_df, avg_Capomulin_vol, on='Mouse ID')
final_Capomulin_vol = avg_Capomulin_vol[['Weight (g)', 'avg_tumor_vol']].drop_duplicates()
final_Capomulin_vol

#scatter plot
x = final_Capomulin_vol['Weight (g)']
y = final_Capomulin_vol['avg_tumor_vol']

plt.scatter(x, y)

plt.xlabel("Weight (g)")
plt.ylabel("Average Tumor Volume (mm3)")
plt.title('Average Tumor Volume by Weight')

plt.show()


# ## Correlation and Regression

# In[235]:


# Calculate the correlation coefficient and linear regression model 

vc_slope, vc_int, vc_r, vc_p, vc_std_err = st.linregress(x, y)
vc_fit = vc_slope * x + vc_int
plt.plot(x,vc_fit,"--")

plt.scatter(x,y)


plt.xlabel("Weight (g)")
plt.ylabel("Average Tumor Volume (mm3)")
plt.title('Average Tumor Volume by Weight')

plt.show()


# In[226]:


#calculate correlation between mouse weight and the average tumor volume for the the Capomulin Regimen

mouse_weight_Capomulin = final_Capomulin_vol['Weight (g)']
avg_tumor_vol_Capomulin = final_Capomulin_vol['avg_tumor_vol']

print(f"The correlation coefficient between mouse weight and the average tumor volume for the the Capomulin Regimen is {round(st.pearsonr(mouse_weight_Capomulin,avg_tumor_vol_Capomulin)[0],2)}")


# In[ ]:




