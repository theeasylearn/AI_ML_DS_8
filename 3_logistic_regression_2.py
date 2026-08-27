# /* Develop Logistic regression example that will predict whether a patient has Diabetes ($y=1$) or Does Not Have Diabetes ($y=0$) based on two input features: BMI ($x_1$) and Age in years ($x_2$). */
import numpy as np 
from sklearn.linear_model import LogisticRegression

#create input dataset
person = np.array([
    [30,30],
    [31,35],
    [32,40],
    [33,41],
    [34,42],
    [35,45],
    [33,50],
    [28,28],
    [27,30],
    [26,30],
    [25,51],
    [24,52],
    [23,55],
]);

#create output dataset
has_diabetes = np.array([0,0,1,1,1,1,1,0,0,0,0,0,0])

#create model 
model = LogisticRegression()

#train model
model.fit(person,has_diabetes)

#create variable that has data to predit 
hansraj_hathi = np.array([[40,45]])

#prediction 
prediction = model.predict(hansraj_hathi)
print("prediction about diabetes of hansraj hathi",prediction)

probability = model.predict_proba(hansraj_hathi)
print("probability of diabetes = ",probability)

tarak_mehta = np.array([[25,50]])

#prediction 
prediction = model.predict(tarak_mehta)
print("prediction about diabetes of tarak_mehta",prediction)

probability = model.predict_proba(tarak_mehta)
print("probability of diabetes = ",probability)

print("Accuracy of model ",model.score(person,has_diabetes))

