import MyMath as m #here m is alias (nick-name) for MyMath
import numpy as np 
height = [4.5,5,5.5,6,6.5,6.7,6.9,7]
height_mean = m.getMean(height)
print("Mean value ",height_mean)
height_result = m.getVariance(height,height_mean) #result is tuple and 0th position has population_variance and 1st value is sample_variable
print(height_result)

weight = [55,60,65,70,80,85,90,95]
weight_mean = m.getMean(weight)
print("Weight Mean ",weight_mean)
weight_result = m.getVariance(weight,weight_mean)
print(weight_result)

covariance_result = m.getCovariance(height, weight)

print("Population Covariance:", covariance_result[0])
print("Sample Covariance:", covariance_result[1])
