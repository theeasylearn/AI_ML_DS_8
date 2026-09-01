import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 

#create dataset 
marks = np.array([
    [78], [65], [45], [92], [56], [88], [71], [34], [99], [62],
    [53], [81], [47], [74], [68], [91], [39], [85], [59], [76],
    [43], [97], [64], [52], [83], [70], [36], [89], [61], [55],
    [94], [48], [73], [67], [82], [41], [58], [96], [63], [77],
    [35], [86], [69], [54], [93], [72], [49], [87], [60], [79],
    [44], [98], [66], [51], [84], [38], [75], [57], [90], [46],
    [80], [33], [95], [68], [42], [71], [88], [53], [62], [99],
    [37], [76], [59], [81], [65], [47], [92], [56], [73], [85],
    [50], [78], [34], [91], [63], [69], [45], [87], [55], [96],
    [61], [74], [40], [83], [58], [89], [52], [67], [79], [48]
]);

#create model 
model = KMeans(n_clusters=3,random_state=42,n_init=1)

#model train 
model.fit(marks)

#print clusters 
labels = model.labels_
print(labels)

#print centroids 
print("centroids ",model.cluster_centers_)
students = ["Aarav", "Vivaan", "Aditya", "Arjun", "Krish", "Rudra", "Dhruv", "Aryan", "Reyansh", "Kabir", "Ayaan", "Vihaan", "Rohan", "Yash", "Harsh", "Dev", "Raj", "Manav", "Kunal", "Parth", "Meet", "Jai", "Darsh", "Neel", "Ved", "Shiv", "Moksh", "Tanish", "Om", "Soham", "Ayush", "Nirav", "Hiten", "Mihir", "Ansh", "Kartik", "Ronak", "Sagar", "Aniket", "Rahul", "Akash", "Nikhil", "Vatsal", "Chirag", "Bhavin", "Hardik", "Tirth", "Maulik", "Jigar", "Het", "Darshan", "Vivek", "Amit", "Karan", "Ritesh", "Nayan", "Kishan", "Bhargav", "Ravi", "Smit", "Akshat", "Manish", "Vishal", "Pratik", "Nirmit", "Yuvraj", "Siddharth", "Abhishek", "Rishabh", "Tejas", "Viren", "Naitik", "Aayush", "Rajesh", "Sachin", "Piyush", "Anuj", "Hemant", "Vijay", "Gaurav", "Mohit", "Varun", "Deep", "Kush", "Rakesh", "Samir", "Akhil", "Mayank", "Rajat", "Suraj", "Prem", "Naman", "Aman", "Ketan", "Dhiren", "Jayesh", "Darshit", "Ronit", "Sahil", "Utsav"]
#we want to display like below 
'''
Aarav has 78 marks and he is excellent  student
Vivaan has 65 marks and he is  average student
Aditya has 40 marks and he is  weak student
'''
for name,score,group in zip(students,marks.flatten(),labels):
    temp = ""
    if group == 0:
        temp = "excellent"
    elif group == 1:
        temp = "average"
    else:
        temp = "weak"
    print(f"{name} has {score} marks and he/she is {temp} student")

#create scatter plot
plt.scatter(marks,labels)
plt.xlabel("student marks")
plt.ylabel("student category")
plt.title("Student performant")
plt.show()