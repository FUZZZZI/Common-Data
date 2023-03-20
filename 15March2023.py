#Day39 - 15Mar2023
#Introduction to Machine Learning

##AI vs Ml vs DL vs DS
#AI: Smart appl that can perform their task w/o any human intervention.
#ML: provides stats tool to learn, analyse, visualize & develop predictive models from data.
#DL: mimic human brain (Multi layered neural network)
# Ex: Object detection, image recognition, chatbot, chatgpt

#Supervised, unsupervised & reinforcement learning

#Types of ML
# Supervised
#  Classification: Binary, multiclass
#  Dependent & Ind features
#  Ex: plyhours, studyhours, paas/fail

#  Regression
#  o/p is cont features
#  Ex: size of house, no of rooms, price

# unsupervised
#  dataset -> clusters or similar groups
#  Ex: customer segmentation


# Semi Supervised
#  Combination of both
#  Ex: netflix

# Reinforcement
#  AI bots play games
#  agent based on env take actions to maximise cumulative reward

#####################
#Train, Validation & Test 
#train the model
#hyper parameter tunning of model
#test the model accuracy
# Ex: Exam - Books; Q&A from other source; Exam Paper

#model should not know the test data - otherwise data leakage will happen.

###################################################
#Day40 - 16Mar2023
#Introduction to Machine Learning

#Bias, Variance, Overfitting & underfitting
#Model performance
#accuracy inc.

#overfitting, underfitting
#overfitting: Model with training dataset give high accuracy but with test low.
# Ex: Muggup
# Low bias & high variance

#underfitting: Model with training dataset give low accuracy and with test low.
# Ex: Not learn for exam
# High bias & high variance

#generalised model: Model with training dataset give high accuracy and with 
#test high.
# Low bias & low variance

#bias vs variance [training vs testing]

###################################################
#Day41 - 17Mar2023
#Feature Engineering

#Handling missing values
# 1. missing completely at random, MCAR
#prob of value being missing does not depend on either observed data or missing data.
# or
# missing values are randomly distributed throughout the dataset and there is no
# systematic reason for why they are missing.

# 2. missing at roandom MAR
# prob of value missing depend only on observed data.

# 3. missing data not at random (MNAR)
# prob of value missing values depend on missing data itself. Missing is not random
# and is dependent on unobserved factors that are associated with missing values

import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
#check missing values
df.isnull().sum()
#delet the rows/datapoints to handle missing values
df.shape
df.dropna().shape                                                               #dropna
#can use inplace=true

#column wise delete
df.dropna(axis=1).shape                 #all columns with missing data are deleted

#Imputation Missing values
# 1. mean value imputation: replace with mean of column
#better for normally distr data
sns.displot(df.age)
#or
sns.displot(df["age"])

sns.histplot(df.age, kde=True)
df["Age Mean"] = df["age"].fillna(df["age"].mean())
#mean() not mean as it is a function
df[["age","Age Mean"]]

# 2. median value imputation - if outliers present
df["Age Median"] = df["age"].fillna(df["age"].median())
df[["age","Age Mean", "Age Median"]]

# 3. mode imputation technique - Categorical values
df.columns
df[df["embarked"].isnull()]
#no relationship at all so MCAR














