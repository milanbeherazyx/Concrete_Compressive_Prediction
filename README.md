# Concrete Compressive Strength Prediction

---------------------------------

# Data Type: multivariate
 
>Abstract: Concrete is the most important material in civil engineering. The concrete compressive strength is a highly nonlinear function of age and  ingredients. These ingredients include cement, blast furnace slag, fly ash, water, superplasticizer, coarse aggregate, and fine aggregate.

---------------------------------
# Sources: 

  `Original Owner and Donor`
  `Prof. I-Cheng Yeh`
  `Department of Information Management` 
  `Chung-Hua University, `
  `Hsin Chu, Taiwan 30067, R.O.C.`
  `e-mail:icyeh@chu.edu.tw`
  `TEL:886-3-5186511`

  `Date Donated: August 3, 2007`
 
---------------------------------

# Data Characteristics:
    
>The actual concrete compressive strength (MPa) for a given mixture under a specific age (days) was determined from laboratory. Data is in raw form (not scaled). 

# Summary Statistics: 

`Number of instances (observations): 1030`
`Number of Attributes: 9`
`Attribute breakdown: 8 quantitative input variables, and 1 quantitative output variable`
`Missing Attribute Values: None`

---------------------------------

# Variable Information:

>Given is the variable name, variable type, the measurement unit and a brief description. The concrete compressive strength is the regression problem. The order of this listing  corresponds to the order of numerals along the rows of the database. 

* `Name -- Data Type -- Measurement -- Description`

* `Cement (component 1) -- quantitative -- kg in a m3 mixture -- Input Variable`
* `Blast Furnace Slag (component 2) -- quantitative -- kg in a m3 mixture -- Input Variable`
* `Fly Ash (component 3) -- quantitative -- kg in a m3 mixture -- Input Variable`
* `Water (component 4) -- quantitative -- kg in a m3 mixture -- Input Variable`
* `Superplasticizer (component 5) -- quantitative -- kg in a m3 mixture -- Input Variable`
* `Coarse Aggregate (component 6) -- quantitative -- kg in a m3 mixture -- Input Variable`
* `Fine Aggregate (component 7) -- quantitative -- kg in a m3 mixture -- Input Variable`
* `Age -- quantitative -- Day (1~365) -- Input Variable`
* `Concrete compressive strength -- quantitative -- MPa -- Output Variable `
---------------------------------

# Past Usage: 

## Main
> 1. I-Cheng Yeh, "Modeling of strength of high performance concrete using artificial  neural networks," Cement and Concrete Research, Vol. 28, No. 12, pp. 1797-1808 (1998).

## Others
>2. I-Cheng Yeh, "Modeling Concrete Strength with Augment-Neuron Networks," J. of Materials in Civil Engineering, ASCE, Vol. 10, No. 4, pp. 263-268 (1998).

>3. I-Cheng Yeh, "Design of High Performance Concrete Mixture Using Neural Networks," J. of Computing in Civil Engineering, ASCE, Vol. 13, No. 1, pp. 36-42 (1999).

>4. I-Cheng Yeh, "Prediction of Strength of Fly Ash and Slag Concrete By The Use of  Artificial Neural Networks," Journal of the Chinese Institute of Civil and Hydraulic  Engineering, Vol. 15, No. 4, pp. 659-663 (2003).

>5. I-Cheng Yeh, "A mix Proportioning Methodology for Fly Ash and Slag Concrete Using Artificial Neural Networks," Chung Hua Journal of Science and Engineering, Vol. 1, No. 1, pp. 77-84 (2003).

>6. Yeh, I-Cheng, "Analysis of strength of concrete using design of experiments and neural networks,": Journal of Materials in Civil Engineering, ASCE, Vol.18, No.4, pp.597-604 ?2006?.

---------------------------------

## Acknowledgements, Copyright Information, and Availability:

### NOTE: Reuse of this database is unlimited with retention of copyright notice for Prof. I-Cheng Yeh and the following published paper:

### I-Cheng Yeh, "Modeling of strength of high performance concrete using artificial neural networks," Cement and Concrete Research, Vol. 28, No. 12, pp. 1797-1808 (1998)

## Life cycle of Machine learning Project

* `Understanding the Problem Statement`
* `Data Collection`
* `Data Checks to perform`
* `Exploratory data analysis`
* `Data Pre-Processing (Feature Engineering and Feature Selection)`
* `Model Training`
* `Hypeparameter Tuning`
* `Choose best model`

# `Understanding the Problem Statement`:
>The quality of concrete is determined by its compressive strength, which is measured using a conventional crushing test on a concrete cylinder. The strength of the concrete is also a vital aspect in achieving the requisite longevity. It will take 28 days to test strength, which is a long period. So, what will we do now? We can save a lot of time and effort by using Data Science to estimate how much quantity of which raw material we need for acceptable compressive strength.



**Data Insights Report**

>I have analyzed the dataset provided and gathered the following insights:

 `1. Missing Values: There are no missing values in the dataset. This means that all the columns have complete data.`

 `2. Duplicates: We have identified 25 duplicate rows in the dataset. It is recommended to investigate these duplicates further to ensure data integrity.`

 `3. Data Types: The dataset consists of numerical data. Most of the columns are of float data type, except for the "Age" column which is of integer data type.`

 `4. Number of Unique Values: Each column in the dataset has a varying number of unique values. The "Cement" column has 280 unique values, "Blast Furnace Slag" has 187 unique values, "Fly Ash" has 163 unique values, "Water" has 205 unique values, "Superplasticizer" has 155 unique values, "Coarse Aggregate" has 284 unique values, "Fine Aggregate" has 304 unique values, "Age" has 14 unique values, and "Compressive Strength" has 938 unique values.`

 `5. Data Statistics: The dataset's statistical summary provides insights into the central tendency, variability, and distribution of the data. The mean and standard deviation for each column give an idea about the average values and the spread of the data. Additionally, percentiles (25%, 50%, and 75%) provide information about the distribution of values.`

 `6. Exploring the Data: We have displayed the first five rows, last five rows, and a sample of five rows from the dataset. This gives you a glimpse of the data and its structure.`

>Based on these insights, we can conclude that the dataset is relatively clean with no missing values. However, there are some duplicate rows that need to be addressed. The data types seem appropriate for the given columns. The unique values in each column highlight the diversity of the dataset. The statistical summary provides an overview of the data distribution and helps identify any outliers or unusual patterns.


# Insights:

1. Skewness:
   - Cement: The distribution of cement is moderately positively skewed, indicating a longer right tail.
   - Blast Furnace Slag: The distribution of blast furnace slag is moderately positively skewed, indicating a longer right tail.
   - Fly Ash: The distribution of fly ash exhibits slightly positive skewness.
   - Water: The distribution of water is approximately symmetric, with negligible skewness.
   - Superplasticizer: The distribution of superplasticizer is highly positively skewed, indicating a significantly longer right tail.
   - Coarse Aggregate: The distribution of coarse aggregate is approximately symmetric, with negligible skewness.
   - Fine Aggregate: The distribution of fine aggregate is approximately symmetric, with negligible skewness.
   - Age: The distribution of age is highly positively skewed, indicating a significantly longer right tail.
   - Compressive Strength: The distribution of compressive strength is approximately symmetric, with negligible skewness.

2. Cement, Blast Furnace Slag, and Fly Ash:
   - The distributions of cement, blast furnace slag, and fly ash are positively skewed, indicating a concentration of lower values and a tail of higher values. This suggests that the majority of data points fall within a specific range, with a few extreme values.

3. Water, Coarse Aggregate, and Fine Aggregate:
   - The distributions of water, coarse aggregate, and fine aggregate are approximately symmetric, indicating a relatively balanced spread of values.

4. Superplasticizer:
   - The distribution of superplasticizer is highly positively skewed, suggesting a significant concentration of lower values and a long tail of higher values. This indicates that the majority of data points have low superplasticizer values, with a few outliers having exceptionally high values.

5. Age:
   - The distribution of age is highly positively skewed, indicating a concentration of lower ages and a tail of higher ages. This suggests that the majority of data points correspond to a relatively young age, with a few instances of significantly higher ages.

6. Compressive Strength:
   - The distribution of compressive strength is approximately symmetric, indicating a relatively balanced spread of values.

>These insights provide an overview of the skewness and distribution characteristics of each variable in the dataset, helping to understand the data's underlying patterns and potential outliers.


# Insights:
 `It is noticed that there is a positive relationship in between Cement and Comressive strength. While there is a negetive relationship in between Water and Comressive strength.`

 `There is a concept of Water Cement Ration in Civil Engineering, the lower the w/c ratio the higher the Compressive strength. So we create a new variable Water Cement Ratio.`

# Conclusion from EDA:
 `Now we can definately see thhat, the lower the w/c ratio the higher the Compressive strength.`

# Model Training Results:

Linear Regression
Model performance for Training set
- Root Mean Squared Error: 9.9734
- Mean Absolute Error: 7.9283
- R2 Score: 0.6401
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 11.5389
- Mean Absolute Error: 8.8262
- R2 Score: 0.5308
===================================


Lasso
Model performance for Training set
- Root Mean Squared Error: 9.9763
- Mean Absolute Error: 7.9320
- R2 Score: 0.6399
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 11.5163
- Mean Absolute Error: 8.8089
- R2 Score: 0.5326
===================================


Ridge
Model performance for Training set
- Root Mean Squared Error: 9.9734
- Mean Absolute Error: 7.9283
- R2 Score: 0.6401
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 11.5388
- Mean Absolute Error: 8.8261
- R2 Score: 0.5308
===================================


ElasticNet
Model performance for Training set
- Root Mean Squared Error: 9.9748
- Mean Absolute Error: 7.9299
- R2 Score: 0.6400
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 11.5238
- Mean Absolute Error: 8.8133
- R2 Score: 0.5320
===================================


K-Neighbors Regressor
Model performance for Training set
- Root Mean Squared Error: 7.3462
- Mean Absolute Error: 5.5699
- R2 Score: 0.8047
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 9.3870
- Mean Absolute Error: 7.2517
- R2 Score: 0.6895
===================================


Decision Tree
Model performance for Training set
- Root Mean Squared Error: 1.0874
- Mean Absolute Error: 0.0934
- R2 Score: 0.9957
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 6.2235
- Mean Absolute Error: 4.0624
- R2 Score: 0.8635
===================================


Random Forest Regressor
Model performance for Training set
- Root Mean Squared Error: 2.0946
- Mean Absolute Error: 1.3515
- R2 Score: 0.9841
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 5.1220
- Mean Absolute Error: 3.4488
- R2 Score: 0.9076
===================================


XGBRegressor
Model performance for Training set
- Root Mean Squared Error: 1.1667
- Mean Absolute Error: 0.3643
- R2 Score: 0.9951
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 5.1097
- Mean Absolute Error: 3.2410
- R2 Score: 0.9080
===================================


CatBoosting Regressor
Model performance for Training set
- Root Mean Squared Error: 1.8157
- Mean Absolute Error: 1.1495
- R2 Score: 0.9881
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 4.2507
- Mean Absolute Error: 2.6615
- R2 Score: 0.9363
===================================


AdaBoost Regressor
Model performance for Training set
- Root Mean Squared Error: 7.1022
- Mean Absolute Error: 5.9548
- R2 Score: 0.8175
----------------------------------
Model performance for Test set
- Root Mean Squared Error: 7.7836
- Mean Absolute Error: 6.2231
- R2 Score: 0.7865
===================================


# Insights:

`Based on the above results, the best model seems to be the Cat Boost Regressor. It achieved the highest mean R2 Score: 0.9363.`

# `Hypeparameter Tuning`

`Accuracy of the model is 93.13.`
`Best hyperparameters: {'depth': 6, 'iterations': 300, 'learning_rate': 0.1}`

# `Best Model Score`
`Training CatBoostRegressor`
`Mean R-squared score: 0.5856641276749954`