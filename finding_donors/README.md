# Machine Learning Engineer Nanodegree
# Supervised Learning
## Project: Finding Donors for CharityML

### Project Overview
In this project, we will apply supervised learning techniques and an analytical mind on data collected for the U.S. census to help CharityML identify people most likely to donate to their cause. We will first explore the data to see how it's recorded. Next, we will apply a series of transformations and preprocessing techniques to manipulate the data into a workable format. We will then evaluate serveral supervised learners of our choice on the data, and consider which is best suited for the solution. Afterwards, we will optimized the model and present it as our solution to CharityML. 

### Project Highlights
This project is designed to get us accquainted with supervised learning algoriths available in sklearn, and to also provide for a method for evaluating just how each model works and performs on a certain type of data. It is important in Machine Learning to understand exactly when and where a certain algorithm should be used. 

## Content

- Data Exploration
  - General Statistic description
  - Feature Exploration
  
- Data Preprocessing
  - Applied logarithmic transform to highly skewed features
  - Normalizing numeric features
  - One-hot encoded categorical features
  
- Evaluate Model Performance
  - Metrics selection
  - Evaluate pros and cons of Decision Tree Classifier, Support Vector Machine and Gradient Boosting Classifier
  - Implement and Compare these three classifiers.
  - <img src="https://user-images.githubusercontent.com/17235054/32567714-1dd2fcda-c48a-11e7-9182-fd4df8781b86.png" width=700 height=400>
  - Selecting the best model and optimized its performance using GridSearch. 
  
- Feature Relevance Observation
  - Extracted feature importance from Adaboost.
  - <img src="https://user-images.githubusercontent.com/17235054/32568143-6a8857b8-c48b-11e7-8b06-683b6711bba6.png" width=400 height=250>
  - Trained classifier with and without feature selection.
  - Compared and analyzed the effect of feature selection. 



### Data

The modified census dataset consists of approximately 32,000 data points, with each datapoint having 13 features. This dataset is a modified version of the dataset published in the paper *"Scaling Up the Accuracy of Naive-Bayes Classifiers: a Decision-Tree Hybrid",* by Ron Kohavi. You may find this paper [online](https://www.aaai.org/Papers/KDD/1996/KDD96-033.pdf), with the original dataset hosted on [UCI](https://archive.ics.uci.edu/ml/datasets/Census+Income).

**Features**
- `age`: Age
- `workclass`: Working Class (Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked)
- `education_level`: Level of Education (Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool)
- `education-num`: Number of educational years completed
- `marital-status`: Marital status (Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse)
- `occupation`: Work Occupation (Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces)
- `relationship`: Relationship Status (Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried)
- `race`: Race (White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black)
- `sex`: Sex (Female, Male)
- `capital-gain`: Monetary Capital Gains
- `capital-loss`: Monetary Capital Losses
- `hours-per-week`: Average Hours Per Week Worked
- `native-country`: Native Country (United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands)

**Target Variable**
- `income`: Income Class (<=50K, >50K)
