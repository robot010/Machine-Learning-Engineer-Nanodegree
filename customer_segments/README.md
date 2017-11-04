# Content: Unsupervised Learning

## Project Overview

In this project, we are going to apply unsupervised techniques on product spending data collected for customers of a wholesale distributor. We aim to identify customer segments hidden in the data. We first explore the data by selecting a small subset to determine if any product categories are highly correlated with one another. Afterwards, we will preprocess the data by scaling each product category and then removing unwanted outliers. With the good, clean data, we apply PCA transformations to the data and implement GMM clustering algorithms to segment the transformed customer data. Finally, we compare the segmentation found with an additional labeling and consider ways this transformation could assist the whole sale distributor with future service. 

## Highlights

This project is designed to get hands-on experience with unsupervised learning and work towards developing conclusions for a potential client on a real-world dataset. We are tring to understand the meaningful relationship hidden in the company's customers and clientele. Being equipped with this information, we would be able to assist a company engineer future products and services that best satisfy the demands of their customers. 


## Data

The customer segments data is included as a selection of 440 data points collected on data found from clients of a wholesale distributor in Lisbon, Portugal. More information can be found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wholesale+customers).

Note (m.u.) is shorthand for *monetary units*.

**Features**
1) `Fresh`: annual spending (m.u.) on fresh products (Continuous); 
2) `Milk`: annual spending (m.u.) on milk products (Continuous); 
3) `Grocery`: annual spending (m.u.) on grocery products (Continuous); 
4) `Frozen`: annual spending (m.u.) on frozen products (Continuous);
5) `Detergents_Paper`: annual spending (m.u.) on detergents and paper products (Continuous);
6) `Delicatessen`: annual spending (m.u.) on and delicatessen products (Continuous); 
7) `Channel`: {Hotel/Restaurant/Cafe - 1, Retail - 2} (Nominal)
8) `Region`: {Lisbon - 1, Oporto - 2, or Other - 3} (Nominal) 
