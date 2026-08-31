''' crate linear regression example using small dataset designed to predict a House Price ($y$ in thousands) based on two features: House Size ($x_1$ in hundreds of sq. ft.) and Number of Bedrooms ($x_2$). 
House Size (x1),    Number of Bedrooms (x2),    "House Price (y in $1,000s)"
120,                 2,                      150
150,                 3,                      200
180,                 3,                      240
200,                 4,                      290
250,                 5,                      350
'''
import numpy as np 
from sklearn.linear_model import LinearRegression

#create input dataset 
house_info = np.array([[120,2],[150,3],[180,3],[200,4],[250,5]])

#output dataset
price = np.array([150,200,240,290,350])

#create model
model = LinearRegression()

#model train 
model.fit(house_info,price)

#predict house price 
house_1 = np.array([[100,2]])
prediction_1 = model.predict(house_1)

#predit house price for another house
house_2 = np.array([[300,10]])
prediction_2 = model.predict(house_2)

print("House 1 price ",round(prediction_1[0]))
print("House 2 price ",round(prediction_2[0]))

