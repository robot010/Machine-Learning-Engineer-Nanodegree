# Content: Unsupervised Learning

## Project Overview

In this project, we are going to apply unsupervised learning techniques on product spending data collected for customers of a wholesale distributor. We aim to identify customer segments hidden in the data. We first explore the data by selecting a small subset to determine if any product categories are highly correlated with one another. Afterwards, we will preprocess the data by scaling each product category and then removing unwanted outliers. With the good, clean data, we apply PCA transformations to the data and implement Gaussian Mixture Model clustering algorithms to segment the transformed customer data. Finally, we compare the segmentation found with an additional labeling and consider ways this transformation could assist the whole sale distributor with future service. 

<img src="https://user-images.githubusercontent.com/17235054/32409747-e0df6b38-c187-11e7-82a1-13c946791803.png" width=800, height=350>

## Highlights

This project is designed to get hands-on experience with unsupervised learning and work towards developing conclusions for a potential client on a real-world dataset. We are tring to understand the meaningful relationship hidden in the company's customers and clientele. Being equipped with this information, we would be able to assist a company engineer future products and services that best satisfy the demands of their customers. 

## Content

- Data Exploration
  - General statistical description.
  - Generate heatmap on three selected samples to get an intuitive understanding of features' relationship.
  - Feature Relevance Analysis using Decision Tree Regressor. 
  - Feature Distribution Visualization by constructing scatter matrix and heatmap for correlation.
  - <img src="https://user-images.githubusercontent.com/17235054/32410431-19ce438e-c196-11e7-9efb-25e03706b908.png"> 
- Data Preprocessing
  - Logarithm Transformation. 
  - Use Turkey's Method to detect Outlier.
- Data Transformation
  - Implement Princial Component Analysis (PCA) on training set, and report explained variance ratio of each dimension. 
  - <img src="https://user-images.githubusercontent.com/17235054/32410641-1ff2b492-c19c-11e7-92a8-f1f843ca45f8.png">
  - PCA feature dimension analysis and calculate the cumulative explained variance ratio to determine how many dimensions are necessary for the problem.
  - Dimension reduction on original data using PCA. 
  - Visualized principal components using biplot. 
  - <img src="https://user-images.githubusercontent.com/17235054/32410740-76c0a12e-c19e-11e7-85c3-9853cc7c3866.png">
- Clustering
  - Quantify the "goodness" of a clustering by calculating each data point's silhouette coefficient
  - Implement Gaussian Mixture Model on data. 
  - Cluster Visualization.
  - <img src="https://user-images.githubusercontent.com/17235054/32410763-c9ed1080-c19e-11e7-8c0a-d6c330ab6e7f.png">
- Conclusion
  - Give suggestions to the wholesale distributor on the change of delivery policy using the above analysis. 
  

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
