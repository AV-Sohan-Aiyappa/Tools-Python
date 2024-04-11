import pandas as pd 

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]}

#Create a Dataframe
df = pd.DataFrame(data)


#importing csv file
csv = pd.read_csv('iris.csv')

#removing string column and finding correlation
dataset = csv.select_dtypes(exclude = "object")
print(dataset.corr())

#replacing values 
csv.loc[7,"Duration"] = 100 

#removing rows 
csv.drop(0, inplace=True)

#remove all rows with null values 
csv.dropna()

#fill new values in empty spaces
csv.fillna(100,inplace=True)

# calculate Mean,Median,Mode 
x = csv["Duration"].mean()
y = csv["Duration"].median()
z = csv["Duration"].mode()[0]


#get info about data 
print(csv.info())


#access a specified value
print(csv.loc[7,"Duration"])














