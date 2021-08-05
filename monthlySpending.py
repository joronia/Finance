import pandas as pd

col_names = ['Date','Description','Debit','Credit','Category']
df = pd.read_csv("./Last_Month_July.csv", names=col_names,skiprows=6).drop(columns='Credit')

sum_of_categories = df.groupby(['Category'])['Debit'].sum().reset_index(name = "Total Amount")

total_spent_from_categories = sum_of_categories['Total Amount'].sum()

sum_of_categories['Total_Monthly_Cost'] = total_spent_from_categories

sum_of_categories['Total_Monthly_Category_Percentage'] = (sum_of_categories['Total Amount'] / sum_of_categories['Total_Monthly_Cost']) * 100

print sum_of_categories