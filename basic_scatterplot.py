""" 
This is a simple program of Scatter Plot.
It shows Relationship between Study Hours and Exam Score
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

data={
    "study_hours":[1,2,3,4,5,6,7,8,9,10],
    "attendance":[55,60,65,70,75,85,90,60,62,60],
    "score":[30,35,45,50,55,65,70,75,80,85],
    "gender":['m','f','m','m','f','f','m','m','f','m']
}
df=pd.DataFrame(data)

print(df)

sns.scatterplot(
    x="study_hours",
    y="score",
    size="attendance",
    hue="gender",
    style="gender",
    palette="coolwarm",
    data=df)
plt.xlabel("Study Hours Per Day")
plt.ylabel("Exam Score")
plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.yticks([10,20,30,40,50,60,70,80,90,100])
plt.title("Study Hours Vs Exam Score")
plt.grid("True")
plt.show()