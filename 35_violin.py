import matplotlib.pyplot as plt 
import pandas as pd 

#load data 
df = pd.read_csv('marks.csv').squeeze()
data = [
    df[df['Division'] == 'A']['Mark'],
    df[df['Division'] == 'B']['Mark'],
    df[df['Division'] == 'C']['Mark'],
    df[df['Division'] == 'D']['Mark'],
    ]
plt.violinplot(data,showmeans=True)
plt.xticks(range(1,5),labels=['A','B','C','D'])
plt.show()