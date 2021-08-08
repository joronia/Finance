import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

col_names = ['Date','Description','Debit','Credit','Category']
df = pd.read_csv("../Personal_Finance/Last_Month_July.csv", names=col_names,skiprows=6).drop(columns='Credit')
df1 = pd.read_csv("../Personal_Finance/category_to_date.csv")
df2 = pd.read_csv("../Personal_Finance/spent_by_month.csv",names=["amount","Month_Year"])

sum_of_categories = df.groupby(['Category'])['Debit'].sum().reset_index(name = "Total Amount")

total_spent_from_categories = sum_of_categories['Total Amount'].sum()

sum_of_categories['Total_Monthly_Cost'] = total_spent_from_categories

sum_of_categories['Total_Monthly_Category_Percentage'] = sum_of_categories['Total Amount'] / sum_of_categories['Total_Monthly_Cost'] * 100

sum_of_categories['Month_year'] = df['Date'].str.split().str[0] + " " + df['Date'].str.split().str[2]

labels = sum_of_categories['Category'].tolist()

percentage = sum_of_categories['Total_Monthly_Category_Percentage'].tolist()

amount_spent_in_month = {'Amount' : [total_spent_from_categories], 'Month_year' : [sum_of_categories['Month_year'].iloc[0]]}

amount_spent_in_month_df = pd.DataFrame(data=amount_spent_in_month)

x_pos = [i for i, _ in enumerate(df2["Month_Year"].tolist())]
energy = df2['amount'].tolist()
plt.bar(df2["Month_Year"].tolist(), energy, color='green')
plt.xlabel("Month")
plt.ylabel("Dollar Amount ($)")
plt.title("Expense per month")

fig1, ax1 = plt.subplots()

ax1.pie(percentage, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, rotatelabels=True)

ax1.axis('equal')

Expenses_Breakdown_Table = pd.pivot_table(df1, values = ['Total Amount'], index = ['Category', 'Month_year'], aggfunc=sum).reset_index()
Expenses_Breakdown_Table.columns = [x.upper() for x in Expenses_Breakdown_Table.columns]
Expenses_Breakdown_Chart = px.line(Expenses_Breakdown_Table, x='MONTH_YEAR', y="TOTAL AMOUNT", title="Expenses Breakdown", color = 'CATEGORY')
Expenses_Breakdown_Chart.update_yaxes(title='Expenses', visible=True, showticklabels=True)
Expenses_Breakdown_Chart.update_xaxes(title='Date', visible=True, showticklabels=True)

with open('../Personal_Finance/category_to_date.csv', 'a') as f:
    f.write('\n') 
sum_of_categories.to_csv('../Personal_Finance/category_to_date.csv',mode='a', header=False)

with open('../Personal_Finance/spent_by_month.csv', 'a') as f:
    f.write('\n') 
amount_spent_in_month_df.to_csv('../Personal_Finance/spent_by_month.csv',mode='a', header=False)

#Expenses_Breakdown_Chart.show()
plt.show()