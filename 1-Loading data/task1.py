import json
import pandas as pd

def task1():

    #reads through the csv
    df = pd.read_csv("/course/data/dataset.csv")

    #splits the number of elements in columns into lists
    categories = df['category'].tolist()

    #finding the number of elements in categories
    num_categories = len(set(categories))

    output = {
        "Number of Products:": df.shape[0],
        "Number of Categories:": num_categories,
    }

    #save ouput to JSON 
    with(open("task1.json", "w")) as f:
        json.dump(output, f)

    return
