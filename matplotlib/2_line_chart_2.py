# step 1 
import matplotlib.pyplot as plt 

#step 2 (create data)
#here score is y 
score = [5, 11, 15, 25, 26, 34, 41, 51, 64, 69,79, 85, 95, 108, 115,124, 134, 141, 159, 169]
#here over is x 
overs = list(range(1,21)) 
print(overs)
# select chart type (line chart)
plt.plot(overs,score)

#customization 
plt.title("Gujarat Titan Score ",fontsize=21,fontweight='bold',loc='left',pad=15)
plt.xlabel('Overs',fontsize=15,fontweight='bold')
plt.ylabel('Runs',fontsize=15,fontweight='bold')
plt.legend(title=['runs'],loc='best')
plt.grid(visible=True,which='both')
#display chart 
plt.show()