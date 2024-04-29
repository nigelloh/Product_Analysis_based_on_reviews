import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def task4():

    # retrieving only the average score of Pet Supplies products
    data_task2 = pd.read_csv('task2.csv')
    new_data2 = data_task2[data_task2.category == 'Pet Supplies']
    df2 = new_data2['average_score']

    # retrieving only the average cost of Pet Supplies products
    data_task3 = pd.read_csv('task3.csv')
    new_data3 = data_task3[data_task3.category == 'Pet Supplies']
    df3 = new_data3['average_cost']

    # combining the data of the average score and average cost together
    result = pd.concat([df2, df3], axis = 1, join='inner')

    # plotting a scatter plot of the relationship between Pet Supplies products of their
    # average review scores and average cost
    result.plot(
        x='average_cost',
        y='average_score',
        kind = 'scatter',
        c='cornflowerblue',
        title='Average Review Score Vs Average Cost for Pet Supplies',
        xlabel='Average Cost',
        ylabel='Average Score'
    )
    
    plt.grid()
    plt.show()

    # saving as a png file
    plt.savefig("task4.png")

    return
