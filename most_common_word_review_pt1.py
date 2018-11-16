import json
import pandas as pd
import random

input_json = "yelp_academic_dataset_review.json"
with open(input_json, 'r') as f:
    data = f.readlines()
    data = list(map(json.loads, data))

def get_review_list(df):
    reviews = list(df['text'])
    reviews = [w.replace("\n", " ") for w in reviews]
    reviews = [w.replace("\r", " ") for w in reviews]
    return reviews

def get_sample(reviews, n):
    return random.sample(reviews, n)

def save_review(reviews, filename):
    with open(filename, "w") as f:
        for item in reviews:
            f.write(f'{item}\n')

df = pd.DataFrame(data)
df_2below_stars = df.loc[df['stars'] <= 2, ['stars','text']]
df_4above_stars = df.loc[df['stars'] >= 4, ['stars','text']]

reviews = get_review_list(df)
reviews_2below_stars = get_review_list(df_2below_stars)
reviews_4above_stars = get_review_list(df_4above_stars)

reviews_10000 = get_sample(reviews, 10000)
reviews_2below_stars_10000 = get_sample(reviews_2below_stars, 10000)
reviews_4above_stars_10000 = get_sample(reviews_4above_stars, 10000)

save_review(reviews_10000, "reviews_10000.txt")
save_review(reviews_2below_stars_10000, "reviews_2below_stars_10000.txt")
save_review(reviews_4above_stars_10000, "reviews_4above_stars_10000.txt")