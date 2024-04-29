## Objective:
The primary objective of this project is to conduct comprehensive data analysis on a dataset comprising product details and customer reviews. Utilizing advanced computational techniques, the project endeavors to extract valuable insights into product performance, pricing dynamics, and sentiment analysis, facilitating informed decision-making processes for stakeholders.

---

Overview

This project aims to perform various data analysis tasks on a dataset containing product information and reviews. The tasks range from basic data loading to advanced text processing and sentiment analysis.

## Task 1: Loading Data

Implemented the `task1()` function in `task1.py` to load the dataset and provide basic statistics in JSON format. This includes counting the number of products and categories in the dataset.

### Task 2: Data Aggregation

Implemented the `task2()` function in `task2.py` to aggregate review data by calculating the average review score for each product. The function ensures that only valid reviews with a review star rating are considered for the calculation. Results are saved to a CSV file named `task2.csv`.

### Task 3: Calculating the Average Product Price

Implemented the `task3()` function in `task3.py` to calculate the average cost for each product. This involves handling various formats of cost data, including single prices and price ranges. Results are saved to a CSV file named `task3.csv`.

### Task 4: Plotting the Average Review Score

Implemented the `task4()` function in `task4.py` to create a plot comparing the average review score with the average price for products in the 'Pet Supplies' category. This visualization helps identify any potential relationship between product price and customer satisfaction.

### Task 5: Comparing Review Scores Between Categories

Implemented the `task5()` function in `task5.py` to generate a plot comparing the mean review scores across different product categories. This analysis provides insights into how review scores vary between product types.

### Task 6: Text Processing

Implemented the `task6()` function in `task6.py` to preprocess review text for sentiment analysis. This involves converting text to lowercase, removing non-alphabetic characters, eliminating stopwords, and generating word bigrams. Results are saved in a JSON file named `task6.json`.

### Task 7: Detecting the Most Indicative Bigrams of Positive Reviews

Implemented the `task7()` function in `task7.py` to calculate log odds ratios for bigrams and identify the most indicative phrases of positive reviews. The function outputs statistics in a CSV file named `task7a.csv` and visualizations in `task7b.png` and `task7c.png`.

### Task 8: Analysis Report

Prepared a comprehensive analysis report summarizing findings from tasks 4, 5, and 7. The report includes interpretations of plots, insights into review sentiment, and reflections on product characteristics. The report is submitted as `task8.pdf`.

---
