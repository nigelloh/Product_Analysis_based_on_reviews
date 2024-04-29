import pandas as pd
import json
import re

def task3():
    output_df = {"ID": [], "category": [], "average_cost": []}

    #read the dataset
    df = pd.read_csv("/course/data/dataset.csv")

    index = 0
    prices = df['cost']
    for one_price in prices:

        # finding the pattern
        check = r'\d+\.\d+'
        list_prices = re.findall(check, one_price)

        # checking if there are 2 values or 1 value in price range
        if len(list_prices) == 2:
            average_price = (float(list_prices[0]) + float(list_prices[1])) / 2.0

        elif len(list_prices) == 1:
            average_price = float(list_prices[0])

        else:
            average_price = 0.00

        output_df["ID"].append(index)
        output_df["category"].append(df["category"][index]) 
        output_df["average_cost"].append(average_price)

        index += 1

    # saving to csv file
    df = pd.DataFrame(data=output_df)
    df.to_csv("task3.csv", index=False, float_format = '%.2f')

    return
