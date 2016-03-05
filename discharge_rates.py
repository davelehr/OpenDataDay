
# coding: utf-8

# In[2]:

# Get total number of discharges by provider 
totals = pd.DataFrame(df.groupby(['Provider Name']).sum()['Total Discharges']).reset_index()

# Get DRG categories of interest 
cats = df.loc[df['DRG Definition'].isin(['308 - CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS W MCC',
                                  '069 - TRANSIENT ISCHEMIA', '280 - ACUTE MYOCARDIAL INFARCTION, DISCHARGED ALIVE W MCC',
                                  '281 - ACUTE MYOCARDIAL INFARCTION, DISCHARGED ALIVE W CC',
                                 '282 - ACUTE MYOCARDIAL INFARCTION, DISCHARGED ALIVE W/O CC/MCC', 
                                 '291 - HEART FAILURE & SHOCK W MCC',
                                 '292 - HEART FAILURE & SHOCK W CC', 
                                 '293 - HEART FAILURE & SHOCK W/O CC/MCC',
                                 '305 - HYPERTENSION W/O MCC',
                                 '637 - DIABETES W MCC',
                                 '638 - DIABETES W CC',
                                 '640 - MISC DISORDERS OF NUTRITION,METABOLISM,FLUIDS/ELECTROLYTES W MCC',
                                 '641 - MISC DISORDERS OF NUTRITION,METABOLISM,FLUIDS/ELECTROLYTES W/O MCC',
                                 '682 - RENAL FAILURE W MCC',
                                 '683 - RENAL FAILURE W CC',
                                 '684 - RENAL FAILURE W/O CC/MCC'])]

# Make it a dataframe with provider info
cats2 = pd.DataFrame(want.groupby(['Provider Name', 'Provider Id', 'Provider State', 
                                  'Provider Zip Code', 'Provider Street Address']).sum()['Total Discharges']).reset_index()

# Merge the two dataframes
merged = pd.merge(totals, cats2, on ='Provider Name')

# Get the percentage
merged['perc'] = merged['Total Discharges_y']/merged['Total Discharges_x']*100

# Rename columns
merged = merged.rename(columns={'Total Discharges_x': 'Total Discharges', 'Total Discharges_y': 'DRG Discharges'})

# Export to Excel
merged.to_excel ('medicare_cleaned.xlsx')

import pandas as pd
import numpy as np

df = pd.read_csv('Medicare_Provider_Charge_Inpatient_DRG100_FY2013.csv')


# In[162]:

# Get total number of discharges by provider 
totals = pd.DataFrame(df.groupby(['Provider Name']).sum()['Total Discharges']).reset_index()

# Get DRG categories of interest 
cats = df.loc[df['DRG Definition'].isin(['308 - CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS W MCC',
                                  '069 - TRANSIENT ISCHEMIA', '280 - ACUTE MYOCARDIAL INFARCTION, DISCHARGED ALIVE W MCC',
                                  '281 - ACUTE MYOCARDIAL INFARCTION, DISCHARGED ALIVE W CC',
                                 '282 - ACUTE MYOCARDIAL INFARCTION, DISCHARGED ALIVE W/O CC/MCC', 
                                 '291 - HEART FAILURE & SHOCK W MCC',
                                 '292 - HEART FAILURE & SHOCK W CC', 
                                 '293 - HEART FAILURE & SHOCK W/O CC/MCC',
                                 '305 - HYPERTENSION W/O MCC',
                                 '637 - DIABETES W MCC',
                                 '638 - DIABETES W CC',
                                 '640 - MISC DISORDERS OF NUTRITION,METABOLISM,FLUIDS/ELECTROLYTES W MCC',
                                 '641 - MISC DISORDERS OF NUTRITION,METABOLISM,FLUIDS/ELECTROLYTES W/O MCC',
                                 '682 - RENAL FAILURE W MCC',
                                 '683 - RENAL FAILURE W CC',
                                 '684 - RENAL FAILURE W/O CC/MCC'])]

# Make it a dataframe with provider info
cats2 = pd.DataFrame(want.groupby(['Provider Name', 'Provider Id', 'Provider State', 
                                  'Provider Zip Code', 'Provider Street Address']).sum()['Total Discharges']).reset_index()

# Merge the two dataframes
merged = pd.merge(totals, cats2, on ='Provider Name')

# Get the percentage
merged['perc'] = merged['Total Discharges_y']/merged['Total Discharges_x']*100

# Rename columns
merged = merged.rename(columns={'Total Discharges_x': 'Total Discharges', 'Total Discharges_y': 'DRG Discharges'})

# Export to Excel
merged.to_excel ('medicare_cleaned.xlsx')

