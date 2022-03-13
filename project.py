#importing libraries
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
#loading data
data = pd.read('retail.txt') #here include your file location
data.head()
#exploring to check data
data.columns
#cleaning data if needed
# Building   apriori model
ao = apriori()#(#here include your cleaned data_set , min_support = 0.05, use_colnames = True)
 #the min support is upto requirement
# any other are also been also implemented as per requirement from here

# The Apriori Technique is just a Machine Learning algorithm used to acquire insight into the structural relationships 
# between many of the things involved. The algorithm's most significant practical use is to propose purchases based just on 
# products currently in the user's basket. And the steps and the sample implementation is enclosed in the above steps. 
# These are implemented in according to jupyternotebook so consider this.