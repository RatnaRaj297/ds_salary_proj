# Salary Predictor for Data Science Jobs: Project Overview:
* Created a tool that estimates the salaries for Data Science jobs (MAE ~ $12.2k) to help data scientist negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium.
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

---
### Code and Resources Used:

**Python Version:** 3.7.6\
**Packages:** Pandas, Numpy, Sklearn, Matplotlib, Seaborn, Selenium, Pickle, Flask\
**For Web Framework requirement:** `pip install -r requirements.txt`\
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905 \
**Flask Article:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

---
### Web Scraping

Tweaked the web scraping repo (github repo above) to scrape over 1000 job listing with their descriptions and salaries offered from glassdoor.com. With each job, I got the following:

+ Job Title
+ Salary Estimate
+ Job Description
+ Rating
+ Company 
+ Location
+ Company Headquarters
+ Company Size 
+ Company Founded Date
+ Type of Ownership
+ Industry
+ Sector
+ Revenue
+ Competitors

---
### Data Cleaning

After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

+ Parsed numeric data out of salary
+ Removed rows without salary
+ Parsed rating out of company text
+ Made a new column for company state
+ Added a column for if the job was at the company’s headquarters
+ Transformed founded date into age of company
+ Made columns for if different skills were listed in the job description:
  + Python
  + R-Studio
  + AWS 
  + Spark
  + Excel
+ Column for number of competitors of a given company 
+ Column for the length of the job description

---
### Exploratorty Data Analysis

I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights

![Image not found](https://github.com/RatnaRaj297/ds_salary_proj/blob/master/eda_images/correlation_heatmap.PNG)
![Image not found](https://github.com/RatnaRaj297/ds_salary_proj/blob/master/eda_images/ownership.PNG)
![Image not found](https://github.com/RatnaRaj297/ds_salary_proj/blob/master/eda_images/size.PNG)
![Image not found](https://github.com/RatnaRaj297/ds_salary_proj/blob/master/eda_images/state.PNG)

---
### Model Building

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. 

+ Multiple Linear Regression - Baseline for the model
+ Lasso Regression - Most of the variables did not show Normal Distribution, hence to smoothen the data
+ Random Forest - Because of the sparsity associated and various dummy variables in the data

---
### Model Performance

The Random Forest model far showed the best results. Below are the MAE obtained for the different models:
+ **Multiple Linear Regression:** 20.77
+ **Lasso Regression:** 20.87
+ **Random Forest:** 12.23

---
### Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.


















































