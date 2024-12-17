# NBA_Draft_Studies

The data pulled in this package comes from the following sources:

[Link to draft data](https://www.basketball-reference.com/draft/NBA_2024.html)

[Link to college standings data](https://www.sports-reference.com/cbb/seasons/men/2025-standings.html)

[Link to Streamlit App](https://nba-draft-analysis.streamlit.app/)

# Package Info

This package provides functions to gather and concatenate NBA Draft data ("get_draft()"). It also has a function to add information based on the athletes' senior years of college ("add_colleges()"). There are 3 functions to analyze the data.

# Data Wrangling Functions

get_draft(start_yr, end_yr): scrapes data on the first round of the NBA draft from each year in the user-specified range. Returns a pandas dataframe.

add_colleges(dataframe): takes the dataframe returned by get_draft and adds stats from their college team to the dataframe. It assumes the player's last year in college was the same year in which they were drafted (which may not always have been the case).

# Analysis Functions

knn_analysis(dataframe): takes the dataframe returned by get_draft and performs two K-Nearest Neigbor analyses, one that uses college stats as predictors and one that does not. It attempts to predict the draft order of the players and compares the accuracy of the two models.

dtree_analysis(dataframe): takes the dataframe returned by get_draft and performs two decision tree analyses, one that uses college stats as predictors and one that does not. It attempts to predict the draft order of the players and compares the accuracy of the two models.

linreg_analysis(dataframe): takes the dataframe returned by get_draft and performs two linear regression analyses, one that uses college stats as predictors and one that does not. It attempts to predict the draft order of the players and compares the rmse of the two models.