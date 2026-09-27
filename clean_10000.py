import numpy as np
import pandas as pd

df=pd.read_csv(r"C:\Users\NISHANT\Downloads\csv_10000_uncleaned.csv")
print(df.shape)
print(df.head(10))
print(df.info())  # trlls about all col
print(df.describe()) # tells about only int or float data col


# age col cleaning
print(df["Age"].isnull().sum()) # 187 null values present
# filterenig age col for valid age
valid_age=df.loc[(df["Age"]>0) & (df["Age"]<100),"Age"] # finding the valid age
avg_age=int(valid_age.mean())  # avg age
df.loc[(df["Age"]<0) | (df["Age"]>100) | (df["Age"].isnull()),"Age"]=avg_age  # assigning the avg_age to invalid data
print(df["Age"].isnull().sum())
print(df[(df["Age"]<0) | (df["Age"]>100)]) # verifing



# Filtering the salary col
print(df["Salary"].isnull().sum()) # 201 have null values
# finding the valid salary
valid_salary=df.loc[(df["Salary"] >0) & (df["Salary"]<100000),"Salary"]
print(valid_salary.isnull().sum()) # verifing query
avg_salary=int(valid_salary.mean())
df.loc[(df["Salary"]<0)  | (df["Salary"]>100000) | (df["Salary"].isnull()),"Salary"]=avg_salary
print(df["Salary"].isnull().sum()) # verifing


#  cleaning Experience_Years column
print(df["Experience_Years"].isnull().sum())  # 149 lines
# valid_Experience_Years finding
valid_Experience_Years=df.loc[(df["Experience_Years"] >=0) & (df["Experience_Years"] <=30),"Experience_Years"]
print(valid_Experience_Years.isnull().sum())
avg_valid_Experience_Years=int(valid_Experience_Years.mean())
df.loc[(df["Experience_Years"] <0) | (df["Experience_Years"] >30) | (df["Experience_Years"].isnull()),"Experience_Years"]=avg_valid_Experience_Years
print(df["Experience_Years"].isnull().sum())


###  cleaning the Gender
print(df["Gender"].unique())
print(df["Gender"].isnull().sum())
df["Gender"]=df["Gender"].str.strip().str.capitalize()
print(df["Gender"].unique())
print(df["Gender"].mode())
mode_gender=df.loc[(df["Gender"].notnull()),"Gender"].mode()[0]
print("gender printing",df.loc[(df["Gender"].notnull()),"Gender"].mode())
df["Gender"]=df["Gender"].fillna(mode_gender)
print(df["Gender"].unique())


# city cleaning
print(df["City"].isnull().sum())

print(df["City"].unique())
df["City"]=df["City"].str.strip().str.title()
print(df["City"].unique())
# finding the mode value
mode_city=df.loc[(df["City"].notnull()),"City"].mode()[0]
print(mode_city)
df.loc[df["City"].isnull(),"City"]=mode_city
print(df["City"].isnull().sum())


# department col
print(df["Department"].isnull().sum())
print(df["Department"].unique())
df["Department"]=df["Department"].str.strip().str.upper()
print(df["Department"].unique())
#fillintg the null values
mode_dept=df.loc[df["Department"].notnull(),"Department"].mode()[0]
print(mode_dept)
df.loc[df["Department"].isnull(),"Department"]=mode_dept
print(df["Department"].isnull().sum())


# cleaning the join_date column
print(df["Join_Date"].isnull().sum()) # 145 null
df["Join_Date"]=pd.to_datetime(df["Join_Date"],errors="coerce") # converting the string into the real date time 
print(df["Join_Date"].isnull().sum())
mode_date=df["Join_Date"].mode()[0] # it ignots the null value if we are try to fine the mode values
print(mode_date)
df.loc[df["Join_Date"].isnull(),"Join_Date"]=mode_date
print(df["Join_Date"].isnull().sum())



# cleaning the email column
print(df["Email"].isnull().sum())
df["Email"]=df["Email"].str.strip().str.lower() # converting all the email into lower case sencetive
df["Email"]=df["Email"].fillna("Unknowe") #fillin the null values
print(df["Email"].isnull().sum())  # verifing
invalid_emails=df.loc[(~df["Email"].str.contains("@",na=False) ) | (~df["Email"].str.contains(r"\.",na=False)),"Email"]  # if we dont use the na= false it treate nan as it is nan
print(invalid_emails.unique())
# fixing the invalid emails
df.loc[df["Email"].str.endswith("@gmail"),"Email"]=df.loc[df["Email"].str.endswith("@gmail"),"Email"]+".com"
print(df.loc[(~df["Email"].str.contains("@",na=False) ) | (~df["Email"].str.contains(r"\.",na=False)),"Email"].unique())
# fixing the remainin invalid values
remain_invalid=df.loc[~(df["Email"].str.contains("@",na=False)) | (~df["Email"].str.contains(r"\.")),"Email"]
df.loc[~(df["Email"].str.contains("@",na=False)) | (~df["Email"].str.contains(r"\.")),"Email"]="unknown_email" # we filled it as unknown
print(df.loc[~(df["Email"].str.contains("@",na=False)) | (~df["Email"].str.contains(r"\.")),"Email"].unique()) # verifing
# cleaning the  name column
print(df["Name"].isnull().sum())


# cleaning the name column
print(df["Name"].isnull().sum()) #201 null values
df["Name"]=df["Name"].fillna("Unknown person")
print(df["Name"].isnull().sum())
df["Name"]=df["Name"].str.strip().str.capitalize()


# customer id
print(df["Customer_ID"].head(30))
print(df["Customer_ID"].dtype)
print(df["City"].isnull().sum())
print(df["Customer_ID"].duplicated().sum())
# finding the combined duplicate values on the basic of id and name
print(df[df[["Customer_ID","Name"]].duplicated(keep="first")])
df=df.drop_duplicates()
df=df.drop_duplicates(["Customer_ID","Name","Email"])
print(df.shape)
print(df[["Customer_ID","Name","Email"]].duplicated().sum()) # deleting the ides on the basic of duplicate ["Customer_ID","Name","Email"]
print(df[df["Customer_ID"]<=0])
print(df["Customer_ID"].isnull().sum())
max_id=int(df["Customer_ID"].max())
# filling missing values
df.loc[df["Customer_ID"].isnull(),"Customer_ID"]=range(max_id+1,max_id+1+df["Customer_ID"].isnull().sum())
print(df["Customer_ID"].isnull().sum())
df["Customer_ID"]=df["Customer_ID"].astype(int)


df=df.to_csv("cleaned_10000.csv")