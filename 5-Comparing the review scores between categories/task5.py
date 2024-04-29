import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

def task5():
    
    data_task2 = pd.read_csv('task2.csv')

    # finding the average review score of each category 
    all_average = data_task2.groupby('category')['average_score'].mean()
    
    # plotting a Bar Chart of the relationship between the categories average review scores
    all_average.plot(
        x = 'category',
        y = 'average_score',
        kind = 'bar'
    )
    
    # adjusting font size and placements of labels
    plt.xticks(fontsize = 6.5)
    plt.xlabel('Categories')
    plt.ylabel('Average Review Score')
    plt.subplots_adjust(bottom=0.4)
    plt.suptitle('Comparison of average review score between products from each category', fontsize=10)
    plt.grid(axis='y')

    # saving as a png file
    plt.savefig("task5.png")

    return

