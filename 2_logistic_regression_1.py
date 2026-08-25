import numpy as np 
from sklearn.linear_model import LogisticRegression

# create data sets 
marks = np.array([[2],[4],[6],[8],[9],[10],[11],[12]])
result = np.array([0,0,1,1,1,1,1,1])

#create object of LogisticRegression model 
model = LogisticRegression()

#train model 
model.fit(marks,result)

print("Model trained.....")


#prediction 
prediction = model.predict([[7]])
print(prediction)

#probability 
probability  = model.predict_proba([[7]])
print(f"probability {probability}")

#prediction 
prediction = model.predict([[5]])
print(f"prediction of 5 hours study {prediction}")

#probability 
probability  = model.predict_proba([[5]])
print(f"probability of 5 hours study {probability}")

#check model performance 
performance = model.score(marks,result)
print(performance)

