import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


gold = pd.read_csv('Gold.csv')

tot = pd.read_csv('Luka.csv')

#del daily_g["Date"]
#daily_g.transpose()


gold.loc[:,'Cost_oil']=tot[['Cost']]
g=gold.drop(labels=['Date'],axis=1)
print(g)
g.plot()
plt.show()

columns=['Date','Cost']
x=gold[columns]
y=gold['Cost_oil']

#print(x)
model=LinearRegression()
model.fit(x,y)
gold['predicted']=model.predict(x)
gold[['Cost_oil','predicted']].plot()
plt.show()

params = pd.Series(model.coef_, index=x.columns)
print(params)