import numpy as np
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
#basic maths operations 
# Both arrays must be of same shape, or be broadcast-compatible.
print(a,b)
print("addition of a and b ",a+b)
print("addition of a and b ",a-b)
print("addition of a and b ",a*b)
print("addition of a and b ",a/b)

#scaler operation 
print("let us add 3 into each value of a ",a+3)
print("let us add multiply 5 with each value of a ",a*3)

#mathematical function
print("Sin value of a's each element ",np.sin(a))
print("cos value of a's each element ",np.cos(a))
print("square value of a's each element ",np.sqrt(a))
print("exp value of a's each element ",np.exp(a))
print("log value of a's each element ",np.log(a))


