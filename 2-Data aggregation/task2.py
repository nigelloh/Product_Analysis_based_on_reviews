import pandas as pd
import json
import re

def task2():
    
    #create a dictionary
    output_df = {"ID": [], "category": [], "average_score": []}

    #read the dataset
    df = pd.read_csv("/course/data/dataset.csv")

    reviews = df['REVIEWLIST']

    index = 0
    #convert Json string into list
    for one_review in reviews:
        one_review = json.loads(one_review)
        
        total_score = 0
        count = 0        
        for phrase in one_review:
            rating = phrase["review_star"]

            #checking for similar pattern
            check = r'a-icon a-icon-star a-star-(\d{1}) review-rating'

            #list of ratings
            list_scores = re.findall(check, rating)
            
            if list_scores:
                total_score += int(list_scores[0])
                count += 1

        if count: 
           average_score = float(total_score) / count

        else:
            average_score = 0.0
        
        output_df["ID"].append(index)
        output_df["category"].append(df["category"][index]) 
        output_df["average_score"].append(average_score)

        index += 1

    # saving to csv file
    df = pd.DataFrame(data=output_df)
    df.to_csv("task2.csv", index=False, float_format = '%.2f')
    
    return
