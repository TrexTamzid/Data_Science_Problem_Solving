"""
Student Scores AnalysisThis script performs basic Exploratory Data Analysis (EDA) using pandas.
Tasks:
1. Create a DataFrame from raw data
2. Calculate average scores per subject
3. Calculate total score for each student
4. Identify the top-performing student
5. Find students below average in Math
6. Add Pass/Fail result based on total score
"""
import pandas as pd

def main():
    data={
        "name":["Luffy","Zoro","Sanji","Nami","Robin","Chooper","Usoop"],
        "math_score":[54,65,70,80,90,45,82],
        "science_score":[65,70,72,65,75,85,75],
        "english_score":[74,80,75,65,82,72,78]
    }
    
    df1=pd.DataFrame(data)
    print("                Student Performance Dataframe:\n",df1,"\n")


    avg_scores=df1[["math_score","science_score","english_score"]].mean(axis=0)
    print("Average Scores:\n",avg_scores,"\n")

    df1["total_score"]=df1[["math_score","science_score","english_score"]].sum(axis=1)
   

    top_student=df1.loc[df1["total_score"].idxmax()]
    print("Top performing Student:\n",top_student,"\n")

    math_avg=df1["math_score"].mean()
    below_math_avg=df1[df1["math_score"]<math_avg]
    print("         Student Below Math Average\n",below_math_avg,"\n")

    df1["result"]=df1["total_score"].apply(lambda x:"pass" if x>180 else "fail")

    print("Final DataFrame\n",df1,"\n")

main()
















