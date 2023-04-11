import pandas as pd
import numpy as np
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement as cr
from sklearn.model_selection import StratifiedShuffleSplit as sss 


#Data analytics Statistics

file = pd.read_csv('C:\\Users\\madhavan.bala\\Documents\\pratice\\DA-statistics.csv')
print(file.head())

print(file.shape)

print("It goes to dataset and search any null value in columns present : ",file.isna().any())

newfile = file.price.fillna(file.price.median())
print(newfile)

percentile = file.price.quantile(1.0) #max value
print(percentile)

actual_remove_data = file[file.price<percentile]
print("Here removes the data",actual_remove_data)

#Permutation and combination

#Permutation
data = [1,2,3]
count = 0
peru = permutations(data,2) #here 2 is the combination of the data EX: (1,2) (2,1) etcc..
for i in list(peru):
    print(i)
    count+=1

print("Number of combinatons : ",count)

data_1 = [1,2,3]
count = 0
peru = combinations(data_1,2) #here 2 is the combination of the data EX: (1,2) (2,1) etcc..
for i in list(peru):
    print(i)
    count+=1
print("Number of combinatons : ",count)

data_1 = [1,2,3]
count = 0
peru = cr(data_1,2) #here the value caluculate itself and moves into right side not a left side num to calculate
for i in list(peru):
    print(i)
    count+=1
print("Number of combinatons : ",count)  


dataset = pd.read_csv("C:\\Users\\madhavan.bala\\Downloads\\Chennai.csv")
print(dataset.shape)
print(dataset.head())
print(dataset.describe())

cols = ['Price','Area']
df = dataset[cols]

#Simple Random Sampling
simple_random_sample = df.sample(n = 10).sort_values(by='Area') #here n represent the number of samples and by is used to choose a type
print(simple_random_sample)  #It generate's the random number of values

sample_mean = round(simple_random_sample['Price'].mean(),3) #3 is for decimal
print(sample_mean)

#Systematic Sampling
normal_index = np.arange(0,len(df)) #It provides a Index value for every dataset

choosed_index = np.arange(0,len(df),step = 5)
systematic_sample = df.iloc[choosed_index]
print(systematic_sample)
systematic_mean =(systematic_sample['Price'].mean(),3)
print(systematic_mean)

#Cluster Sampling

n = 5
df['Cluster_sampling'] = np.repeat([range(1,n+1)],len(df)/n)
index = []

for i in range(0,len(df)):
    if df['Cluster_sampling'] %2 == 0:
        index.append(i)

cluster_sampling = df.iloc[index]
mean_cluster_sampling = round(cluster_sampling['price'].mean(),3)
print("Mean ofcluster : ",mean_cluster_sampling)
print(cluster_sampling)

#Stratified Random sample
df['strata'] = np.repeat([1,2],len(df / 2))
indexes = []

for i in range(0,len(df)):
    indexes.append(i)

startified_random_sample = df.iloc['indexes']
print(startified_random_sample)

#set the split criteria
split = sss(n_splits = 1,test_size = 8)

#perform data frame split
for x,y in split.split(df,df['strata']): #strata is like subcats
    startifiedrandom_sample = df.iloc[y].sort_values(by = 'price')

print(startifiedrandom_sample)