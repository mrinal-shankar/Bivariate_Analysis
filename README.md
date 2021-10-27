# Bivariate_Analysis

# Introduction
This package calculates weight of evidence (woe) and information value (iv) for all features in provided data. The woe sheet is also called 'fineclassing' data, where the features are divided in 10 equal buckets (deciles) and for each decile woe is calculated. This helps to understand the significance of feature w.r.t to target feature without any interaction of other features. The insights from this analysis can be combined with feature importance of ml algorithm to select the best features for further model iteration. It is widely used for 'feature selection' when the number of features are large (> 50).
The woe results can be used to draw logit plots to check the monotonocity of features. Further, this can be used to coarse-class (binning the deciles of feature). These results will be added later in further enhancements or in a different package

# Input
One needs to input the dataframe containing features and target variable, and the name of target feature

# Results
The output contains two dataframes - woe result and iv result. The iv sheet has two columns - feature and information value and is sorted in descending order of iv
The woe result contains the below columns-
1. feature - Name of feature.
2. type - Numeric or object
3. decile - Decile of feature (1 to 10)
4. min - Min value of feature in a decile
5. max - Max value of feature in a decile
6. cnt - No. of observations in a decile
7. target - Sum of targets in a decile
8. target_rate - Target rate in a decile
9. target_pct - Percentage of target in a decile to total targets in the data
10. nontarget_pct - Percentage of non-target in a decile to total non-targets in the data
11. woe - Weight of evidence
12. iv - Information value

# Package
woe-iv

# Contact
Mrinal Shankar (https://github.com/mrinal-shankar)
