import sys
import json
import pandas as pd

review_fn = "data/yelp_academic_dataset_review.json"

with open(review_fn, 'r', encoding='UTF-8') as f:
    rev_data = f.readlines()
    # this line below may take at least 8-10 minutes of processing for 4-5 million rows. It converts all strings in list to actual json objects. 
    rev_data = list(map(json.loads, rev_data))
    
rev_df = pd.DataFrame(rev_data)

business_fn = 'data/yelp_academic_dataset_business.json'

with open(business_fn, 'r', encoding='UTF-8') as f:
    bus_data = f.readlines()
    # this line below may take at least 8-10 minutes of processing for 4-5 million rows. It converts all strings in list to actual json objects. 
    bus_data = list(map(json.loads, bus_data))
    
bus_df = pd.DataFrame(bus_data)[['business_id','categories','city','name','review_count','stars']]

bus_df = bus_df[bus_df.categories.str.contains('Restaurant|Food', na=False)]

rest_df = rev_df.merge(bus_df, how='inner', left_on='business_id', right_on='business_id')

rest_df.to_csv('yelp_business_and_reviews', sep='\t', encoding='utf-8')