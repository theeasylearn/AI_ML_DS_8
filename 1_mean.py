import MyMath as m #here m is alias (nick-name) for MyMath
import numpy as np 
height = [4.5,5,5.5,6,6.5,6.7,6.9,7]
# height_mean = m.getMean(height)
# print("Mean value ",height_mean)
# height_result = m.getVariance(height,height_mean) #result is tuple and 0th position has population_variance and 1st value is sample_variable
# print(height_result)

weight = [55,60,65,70,80,85,90,95]
# weight_mean = m.getMean(weight)
# print("Weight Mean ",weight_mean)
# weight_result = m.getVariance(weight,weight_mean)
# print(weight_result)

# #find co-variance 
# height_co_variance = round(height_result[0] / weight_result[0],2)
# weight_co_variance = round(weight_result[0] / height_result[0])

# print(height_co_variance,weight_co_variance)
covariance = np.cov(height,weight)
print("covariance",covariance)