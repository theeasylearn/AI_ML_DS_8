# step 1 
import matplotlib.pyplot as plt 

#step 2 (create data)
#here score is y 
score = [5, 11, 15, 25, 26, 34, 41, 51, 64, 69,79, 85, 95, 108, 115,124, 134, 141, 159, 169]
#here over is x 
overs = list(range(1,21)) 
print(overs)
#set dimension of the chart(size) (must be set before plot method called)
plt.figure(figsize=(14,14))
# select chart type (line chart)
plt.plot(overs,score,linewidth=3,marker='o',color='red',linestyle='-.')

#customization 
plt.title("Gujarat Titan Score ",fontsize=21,fontweight='bold',loc='left',pad=15)
plt.xlim(left=1,right=20)
plt.xticks(ticks=overs)
plt.yticks(ticks=range(0,200,5))
plt.xlabel('Overs',fontsize=15,fontweight='bold')
plt.ylim(bottom=1,top=200)
plt.ylabel('Runs',fontsize=15,fontweight='bold')
plt.legend(title=['runs'],loc='best')
plt.grid(visible=True,which='both')
#display chart 
plt.show()