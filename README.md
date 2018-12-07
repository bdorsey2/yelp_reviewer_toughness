# Yelp Reviewer Toughness Classification

This repository documents the creation of a Machine Learning model to classify Yelp Reviewers as hard, medium, or easy reviewers.   While a lot of work has been done on the Yelp dataset we used, most of it had focused on restaurants, not users. 

After exploring the data, we decided to join the business and reviews tables to calculate an average review star delta for each reviewer, an average of the difference between the restaurant's stars on Yelp and the stars the reviewer gave the restaurant.   

Then we classed reviewers with an average star delta of +0.5 stars (one standard deviation) above the restaurant's stars as easy reviewers, and reviewers with an average star delta of more -0.5 as hard reviewers, and the rest as medium. 

The most performant models were MultiNomial Logistic Regression, Support Vector Machine, and Passive Aggressive Classifier. We performed grid searches across models and our choice of vectorizer to find optimal hyperparameters. 

MultiNomial Logistic Regression performed the best overall.   Besides code for our final models, we’ve included our data processing, exploratory data analysis, and preliminary models.

Main project notebook files:

yelp_data_processing.ipynb - pre-processing code

hard_easy_reviewer_model-v2.ipynb - modeling code

cust_stop_words.py - custom stop words set

plots.py - finalized plots built from pre processing code

yelp_deck_v2.pdf - Presentation slides

DataSet: https://www.yelp.com/dataset

Contributors: Evan Calkins,  Xu Lian, Brian Dorsey, and Quinn Keck 
