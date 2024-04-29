import pandas as pd 
import json
from utils import *

def task6():

    #read data from dataset.csv
    df = pd.read_csv("/course/data/dataset.csv")

    list_scores = []
    review_comments = []
    review_score = 0

    reviews = df["REVIEWLIST"]
    
    # convert the json strings to list 
    for one_review in reviews:
        one_review = json.loads(one_review)

        # finding the score for each review
        for phrase in one_review:
            rating = phrase["review_star"]
            check = r'a-icon a-icon-star a-star-(\d{1}) review-rating'
            
            # returns the review score in a list
            list_scores = re.findall(check, rating)
            #print(list_scores)
            if list_scores:
                review_score = int(list_scores[0])
                
                # processing the review body
                body = phrase["review_body"]
                bigram = processing(body)
            
            # storing the review score and bigrams in dictionaries 
            review_dict = {
                'score': review_score,
                'bigrams': bigram
            }

            # appending the dictionaries into a list
            review_comments.append(review_dict)

    #save ouput to JSON 
    with(open("task6.json", "w")) as f:
        json.dump(review_comments, f)
        

    return
