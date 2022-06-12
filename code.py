import pandas as pd
df=pd.read_csv("C:/Users/mhrat/OneDrive/Desktop/python/mean,median,mode/SOCR-HeightWeight.csv")
height=df["Height(Inches)"].tolist()
sum=0
for H in height:
    sum=sum+H
mean=sum/len(height)
print(mean)
