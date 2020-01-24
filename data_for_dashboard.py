import pandas as pd 
data = pd.read_csv("final_121_weightages.csv")

print(data.columns)
for i in data.columns :
	print(i)
data = data.groupby('regional_code')['Quantity-deliver-percent_y','Difference_in_days','net_price_ratio'].mean()
data = data.reset_index()
print(data)
data.to_csv("data.csv")

# data =data.groupby('Region_code')['Qunatit',]