import numpy as np
from sklearn.linear_model import LinearRegression

x=np.array([[20],[25],[30],[35],[40]])
y=np.array([200,300,400,500,600])

model=LinearRegression()
model.fit(x,y) #model is getting trained
print("Model Trained")
prediction=model.predict([[32]]) #model predicts and saves it
print("Prediction",prediction)