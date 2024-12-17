.. NBA_Draft documentation master file, created by
   sphinx-quickstart on Sat Dec 14 19:42:06 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NBA_Draft documentation
=======================

NBA_Draft is a Python package inspired by the difficulty of finding datasets that combine college statistics with NBA Draft data. This package streamlines the process of collecting, enriching, and analyzing NBA Draft data, enabling deeper insights into player performance and draft outcomes.

Key Features
Data Wrangling

get_draft(start_yr, end_yr): Scrape first-round NBA Draft data for a specified year range and return it as a Pandas DataFrame.
add_colleges(dataframe): Enrich the draft data with college team statistics based on players' senior years.
Analysis Tools

knn_analysis(dataframe): Perform K-Nearest Neighbor analyses to predict draft order with and without college stats.
dtree_analysis(dataframe): Conduct decision tree analyses to predict draft order, comparing models with and without college stats.
linreg_analysis(dataframe): Run linear regression models to predict draft order and compare RMSE values.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   nba_draft
