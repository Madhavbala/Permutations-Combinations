
from scipy.stats import binom
import matplotlib.pyplot as plt

num_of_trials = 10
poss_of_head  = 0.5
binom_probability = [binom.pmf(i,num_of_trials,poss_of_head)for i in range (11)]
plt.stem(list(range(11)),binom_probability)

from scipy.stats import poisson
rate = 3.3
poisson_probability = [poisson.pmf(i,rate)for i in range(15)]
plt.stem(list(range(15)),poisson_probability)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()

from numpy import random
uni_dis = random.uniform(size=(10,1))
plt.stem(list(range(10)),uni_dis)



