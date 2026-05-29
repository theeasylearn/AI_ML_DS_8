# step 1 
import matplotlib.pyplot as plt 

#step 2 (create data)
#here score is y 
score = [5, 11, 15, 25, 26, 34, 41, 51, 64, 69,79, 85, 95, 108, 115,124, 134, 141, 159, 169]
#here over is x 
overs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# select chart type (line chart)
plt.plot(overs,score)

#customization 
plt.title("Gujarat Titan Score ")
plt.xlabel('Overs')
plt.ylabel('Runs')

#display chart 
plt.show()