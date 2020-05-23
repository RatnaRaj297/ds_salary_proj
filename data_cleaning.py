# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:00:56 2020

@author: Ratnaraj
"""
import pandas as pd

df = pd.read_csv('raw_data.csv')



df = df[df['Salary Estimate'] != '-1']
df.drop('Unnamed: 0',axis=1,inplace=True)


# Salary Parsing
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$','') )   

df['min_salary'] = minus_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df['min_salary']+df['max_salary'])/2


# Company name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3] , axis =1 )


# State Field 
for i in range(df.shape[0]):
    try:
        df.loc[i,'state_txt'] = df.loc[i,'Location'].split(',')[1].strip()
    except:
        df.loc[i,'state_txt'] = df.loc[i,'Location'].split(',')[0].strip()
    
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0,axis=1)

# Age of Company 
df['age_company'] = df['Founded'].apply(lambda x: 2020-x if x>0 else -1)

# Parsing of job description (Python, R-studio) 

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0 )
#print(df.python_yn.value_counts())

#spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0 )
#print(df.spark_yn.value_counts())

#r-sutdio
df['rstudio_yn'] = df['Job Description'].apply(lambda x: 1 if 'r-studio' in x.lower() or 'r studio' in x.lower() else 0 )
#print(df.rstudio_yn.value_counts())

#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0 )
#print(df.aws_yn.value_counts())

#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0 )
#print(df.excel_yn.value_counts())

#Saving the Data
df.to_csv('processed_data.csv')