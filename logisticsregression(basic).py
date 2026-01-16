import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
data={
    "hours":[1,2,3,4,5,6,7,8],
    "pass":[0,0,0,0,1,1,1,1]
}
df=pd.DataFrame(data)
x=df[["hours"]] #fetaure must be 2D.Thats why Double Bracket
y=df["pass"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test) #for evaluation

print("Accuracy:",accuracy_score(y_test,y_pred))
print("Confusion Matrix:\n",confusion_matrix(y_test,y_pred))
print("Classification report:",classification_report(y_test,y_pred))

hours=[[5]]
prediction=model.predict(hours)
probability=model.predict_proba(hours)
print("prediction:",prediction)
print("Probability",probability)
