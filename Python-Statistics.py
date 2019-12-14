#------------------------------------From Learning Python 3 Library------------
#----------------------------------------Statistics Module---------------------

# Importing statistics module for statistics functions
import statistics
# Importing math module to prove results from statistics function were correct
import math

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

#---------------------------------------Statistics Definitions-----------------
# Mean-Average
# Median-Midpoint
# Mode-Most frequent value
# Variance of Standard Deviation-Variance of the squared differences from the mean
#----How varied is our data
# Standard Deviation-Square root of the variance

print(statistics.mean(agesData))
print(statistics.mode(agesData))
print(statistics.median(agesData))
print(sorted(agesData))

print(statistics.variance(agesData))
print(statistics.stdev(agesData))
#proving standard deviation above ^
print(math.sqrt(statistics.variance(agesData)))

