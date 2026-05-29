import matplotlib.pyplot as plt
import numpy as np 
data = [31, 33, 35, 37, 39, 41, 43, 32, 34, 36, 38, 40, 42, 44, 46, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 30, 45, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 98, 100, 29, 37, 44, 50, 58, 66, 74, 82, 90, 94, 31, 39, 47, 54, 62, 70, 78, 86, 93, 97, 33, 41, 49, 57, 65, 73, 81, 89, 95, 99, 35, 43, 51, 59, 67, 75, 83, 91, 96, 100, 70, 78, 86, 93, 97, 33, 41, 49, 57, 65, 73, 81, 89, 95,70, 78, 86, 93, 97, 33, 41, 49, 57, 65, 73, 81, 89, 95]

#list convert into numpy array
marks = np.array(data)

plt.hist(marks,density=False,bins=10,color='blue',alpha=0.5,label='Student performance')

plt.xlabel('marks range')
plt.ylabel('no of students')
plt.show()