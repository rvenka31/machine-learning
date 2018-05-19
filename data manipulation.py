import pandas as pd
import numpy as np
data=pd.read_csv("/Users/mac/Downloads/crosstab.csv")

#find missing values
data.isnull().sum()


#Number of values unique to each columns
print("Account size unique value counts\n",data.Account_Size.value_counts())
print("Recommend unique value counts\n",data.Recommend.value_counts())

#crosstab
pd.crosstab(data.Account_Size,data.Recommend)
pd.crosstab(data.Account_Size,data.Recommend,margins=True)

#pivot table

data=pd.read_excel("/Users/mac/Downloads/sales-funnel.xlsx")
pd.pivot_table(data,index=["Rep"])

#Baseball data set

allstar_data=pd.read_csv("/Users/mac/Downloads/baseballdatabank-2017.1/core/AllstarFull.csv")
player_awards=pd.read_csv("/Users/mac/Downloads/baseballdatabank-2017.1/core/AwardsPlayers.csv")
player_college=pd.read_csv("/Users/mac/Downloads/baseballdatabank-2017.1/core/CollegePlaying.csv")
halloffame=pd.read_csv("/Users/mac/Downloads/baseballdatabank-2017.1/core/HallOfFame.csv")
player_salary=pd.read_csv("/Users/mac/Downloads/baseballdatabank-2017.1/core/Salaries.csv")

-------------------
# combining data
# Merge player awards & college to a single table based on the playerID
-------------------
star_alumini=pd.merge(player_awards,player_college,on='playerID')
star_alumini=star_alumini[star_alumini.awardID.isin(['TSN All-Star','TSN Major League Player of the Year','World Series MVP'])]
star_alumini.head()
star_alumini.awardID.value_counts()

-------------------
#pivot table
#Create a pivot to display the number of individual awards won colleges
-------------------

pvt=pd.pivot_table(star_alumini,index= ['schoolID','awardID'],values='playerID',aggfunc=np.count_nonzero,fill_value=0,margins=True)
pvt.head(10)


