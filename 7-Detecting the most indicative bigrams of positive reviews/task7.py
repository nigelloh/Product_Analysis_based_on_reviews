import pandas as pd
import json
import matplotlib.pyplot as plt
import math
from collections import Counter

def task7():
    lor_word_dict = {"bigram": [], "log_odds_ratio": []}

    with open('task6.json') as data_task6:
        score_and_bigrams = json.load(data_task6)

    pos_reviews = []
    neg_reviews = []

    number_pos = 0
    number_neg = 0 
    
    for one_set in score_and_bigrams:
        review_bigram = one_set['bigrams']
        review_score = one_set['score']
    
    # checking if the review is positive   
        if review_score == 5:
            for bigram in review_bigram:
                pos_reviews.append(bigram)
            number_pos += 1

        # checking if the review is negative
        elif review_score == 1:
            for bigram in review_bigram:
                neg_reviews.append(bigram)
            number_neg += 1

    # finding all sorts of bigrams
    all_pos_reviews = set(pos_reviews)
    all_neg_reviews = set(neg_reviews)
    all_bigrams = all_pos_reviews | all_neg_reviews

    # finding the number occurences of each positive and negative reviews
    count_pos = Counter(pos_reviews)
    count_neg = Counter(neg_reviews)

    # finding number of positive/negative reviews containing bigrams
    for one_bigram in all_bigrams:
        final_num_pos = count_pos[one_bigram]
        final_num_neg = count_neg[one_bigram]

        # probability equation
        pos_prob = float(final_num_pos/number_pos)
        neg_prob = float(final_num_neg/number_neg)

        # excluding reviews that have 0 or 1 as their probaility 
        if (pos_prob == 0.0) or (pos_prob == 1.0) or (neg_prob == 0.0) or (neg_prob == 1.0):
            continue

        # calculating the positive and negative odds of bigram
        pos_odds = pos_prob / (1 - pos_prob)
        neg_odds = neg_prob / (1 - neg_prob)

        # finding the odds ratio
        odds_ratio = pos_odds/neg_odds

        # returning log odds ration value
        log_odds_ratio = math.log10(odds_ratio)

        lor_word_dict["bigram"].append(one_bigram)
        lor_word_dict["log_odds_ratio"].append(log_odds_ratio)


    df = pd.DataFrame(data=lor_word_dict)
    df.sort_values(by = ["log_odds_ratio", 'bigram'], inplace=True)
    df.to_csv("task7a.csv", index=False, float_format='%.4f')

    # complete subtask 7b
    fig, ax = plt.subplots()
    ax.hist(df["log_odds_ratio"], bins = 40)
    fig.suptitle("Frequency of Log Odds Ratio for Reviews for Every Distinct Bigram")
    ax.set_xlabel("Log Odds Ratio for Review")
    ax.set_ylabel("Frequency")
    plt.grid()
    fig.savefig("task7b.png")

    # complete subtask 7c
    df2 = pd.concat([df.nsmallest(10, 'log_odds_ratio'), df.nlargest(10, 'log_odds_ratio')])
    df2 = df2.sort_values('log_odds_ratio')
    fig, ax = plt.subplots()
    ax.bar(list(df2['bigram'].values), list(df2['log_odds_ratio'].values))
    fig.suptitle("Top 10 bigrams with the highest odds ratios and top 10 bigrams with the lowest odds ratios", fontsize = 9.5)
    ax.set_xlabel("Bigrams")
    ax.set_ylabel("Log Odds Ratio for Reviews")
    plt.xticks(fontsize=6.5, rotation=90)
    plt.subplots_adjust(bottom=0.35)
    plt.grid(axis = 'y')
    fig.savefig("task7c.png")

    return
