# /* Develop Linear regression example that will predict marks of student base upon daily study hours. */
import numpy as np 
from sklearn.linear_model import LinearRegression

#create input dataset
study_hours = np.array([[1.0],[1.5],[2.0],[2.5],[3.0],[3.5],[4.0],[4.5],[5.0],[5.5],[6.0],[6.5]])

#create output dataset
marks = np.array([30,35,40,45,49,52,55,60,65,70,75,80])


#create model 
model = LinearRegression()


#model train in input dataset
model.fit(study_hours,marks)

#predict marks on dataset
hours = int(input("Enter mohan study hours"))
mohan = np.array([[hours]])
prediction = model.predict(mohan)

print("approximate marks of mohan will be",round(prediction[0],2))

