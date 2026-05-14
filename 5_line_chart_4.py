# step 1 
import matplotlib.pyplot as plt 

#step 2 (create data)
#here score is y 
bhavnagar_april_temps = [
    37.2, 36.7, 34.4, 34.4, 35.0, # April 1 - 5
    36.7, 36.7, 35.6, 35.6, 38.3, # April 6 - 10
    40.0, 40.6, 41.1, 41.7, 40.6, # April 11 - 15
    40.6, 41.1, 41.7, 40.0, 40.0, # April 16 - 20
    41.1, 40.6, 41.7, 42.2, 43.9, # April 21 - 25
    45.0, 44.4, 43.3, 42.8, 41.7  # April 26 - 30
]
dwarka_april_temps = [
    32, 32, 31, 32, 34, 34, 33, 35, 36, 39, 
    39, 40, 40, 39, 39, 39, 39, 38, 39, 39, 
    38, 37, 40, 41, 42, 43, 41, 39, 39, 39
]
#here over is x 
days = list(range(1,31)) 
#set dimension of the chart(size) (must be set before plot method called)
plt.figure(figsize=(14,8))
# select chart type (line chart)
plt.plot(days,bhavnagar_april_temps,linewidth=2,marker='o',markersize=5,color='red',linestyle='-')
plt.plot(days,dwarka_april_temps,linewidth=2,marker='^',markersize=5,color='blue',linestyle='--')
#customization 
plt.title("Bhavnagar & Dwaraka temperature  ",fontsize=21,fontweight='bold',loc='left',pad=15)
plt.xlim(left=1,right=20)
plt.xticks(ticks=days)
plt.yticks(ticks=range(0,50))
plt.xlabel('day',fontsize=15,fontweight='bold')
plt.ylim(bottom=10,top=50)
plt.ylabel('temperature',fontsize=15,fontweight='bold')
plt.legend(loc='best')
plt.grid(visible=True,which='both')
#display chart 
plt.show()