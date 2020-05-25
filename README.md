# Salary Predictor for Data Science Jobs: Project Overview
* Created a tool that estimates the salaries for Data Science jobs (MAE ~ $12.5k) to help data scientist negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium.
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

### Code and Resources Used:
**Python Version:** 3.7.6
**Packages:** Pandas, Numpy, Sklearn, Matplotlib, Seaborn, Selenium, Pickle, Flask
**For Web Framework requirement:** `pip install -r requirements.txt`
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
**Flask Article:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

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




