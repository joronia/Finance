import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import os

def writeDataToCSV():
    col_names = ['Date','Description','Debit','Credit','Category']
    df = pd.read_csv("../Personal_Finance/Last_Month_July.csv", names=col_names,skiprows=6).drop(columns='Credit')
    income_df = pd.read_csv("../Personal_Finance/income_july.csv", names=['Date','Description','Category','Tags','Amount'],skiprows=1).drop(columns='Tags')
    
    df1 = None
    df2 = None
    df3 = None
    
    income_df['Month_Year'] = df['Date'].str.split().str[0] + " " + df['Date'].str.split().str[2]
    income_agg_df = income_df.groupby(['Month_Year'])['Amount'].sum()

    sum_of_categories = df.groupby(['Category'])['Debit'].sum().reset_index(name = "Total Amount")

    total_spent_from_categories = sum_of_categories['Total Amount'].sum()

    sum_of_categories['Total_Monthly_Cost'] = total_spent_from_categories

    sum_of_categories['Total_Monthly_Category_Percentage'] = sum_of_categories['Total Amount'] / sum_of_categories['Total_Monthly_Cost'] * 100

    sum_of_categories['Month_year'] = df['Date'].str.split().str[0] + " " + df['Date'].str.split().str[2]
    
    percentage = sum_of_categories['Total_Monthly_Category_Percentage'].tolist()

    labels = sum_of_categories['Category'].tolist()

    amount_spent_in_month = {'Amount' : [total_spent_from_categories], 'Month_year' : [sum_of_categories['Month_year'].iloc[0]]}

    amount_spent_in_month_df = pd.DataFrame(data=amount_spent_in_month)

    if os.stat("../Personal_Finance/category_to_date.csv").st_size > 0:
      df1 = pd.read_csv("../Personal_Finance/category_to_date.csv",names=["index","Category","Total Amount","Spent","Percentage","Month_year"])
      monthYearList = df1['Month_year'].tolist()
      if sum_of_categories['Month_year'].iloc[0] not in monthYearList:
        with open('../Personal_Finance/category_to_date.csv', 'a') as f:
          f.write('\n') 
          sum_of_categories.to_csv('../Personal_Finance/category_to_date.csv',mode='a', header=False)
          df1 = pd.read_csv("../Personal_Finance/category_to_date.csv",names=["index","Category","Total Amount","Spent","Percentage","Month_year"])
    else:
       with open('../Personal_Finance/category_to_date.csv', 'a') as f:
          f.write('\n') 
          sum_of_categories.to_csv('../Personal_Finance/category_to_date.csv',mode='a', header=False)
          df1 = pd.read_csv("../Personal_Finance/category_to_date.csv",names=["index","Category","Total Amount","Spent","Percentage","Month_year"])
    
    if os.stat("../Personal_Finance/spent_by_month.csv").st_size > 0:
      df2 = pd.read_csv("../Personal_Finance/spent_by_month.csv",names=["amount","Month_Year"])
      monthYearList = df2['Month_Year'].tolist()
      if sum_of_categories['Month_year'].iloc[0] not in monthYearList:
        with open('../Personal_Finance/spent_by_month.csv', 'a') as f:
          f.write('\n') 
          amount_spent_in_month_df.to_csv('../Personal_Finance/spent_by_month.csv',mode='a', header=False)
          df2 = pd.read_csv("../Personal_Finance/spent_by_month.csv",names=["amount","Month_Year"]) # We need to reread the file for new changes
    else:
       with open('../Personal_Finance/spent_by_month.csv', 'a') as f:
          f.write('\n') 
          amount_spent_in_month_df.to_csv('../Personal_Finance/spent_by_month.csv',mode='a', header=False)
          df2 = pd.read_csv("../Personal_Finance/spent_by_month.csv",names=["amount","Month_Year"])
    
    if os.stat("../Personal_Finance/income_by_month.csv").st_size > 0:
      df3 = pd.read_csv("../Personal_Finance/income_by_month.csv",names=['Month_Year','amount'])
      monthYearList = df2['Month_Year'].tolist()
      if sum_of_categories['Month_year'].iloc[0] not in monthYearList:
        with open('../Personal_Finance/income_by_month.csv', 'a') as f:
          f.write('\n') 
          income_agg_df.to_csv('../Personal_Finance/income_by_month.csv',mode='a', header=False)
          df3 = pd.read_csv("../Personal_Finance/income_by_month.csv",names=['Month_Year','amount']) # We need to reread the file for new changes
    else:
       with open('../Personal_Finance/income_by_month.csv', 'a') as f:
          f.write('\n') 
          income_agg_df.to_csv('../Personal_Finance/income_by_month.csv',mode='a', header=False)
          df3 = pd.read_csv("../Personal_Finance/income_by_month.csv",names=['Month_Year','amount'])

    showGraphs(labels,percentage,df1,df2,df3)

def showGraphs(labels,percentage,df1,df2,df3):
    
    energy = df2['amount'].tolist()
    plt.bar(df2["Month_Year"].tolist(), energy, color='red')
    plt.axhline(df2['amount'].mean(),color='purple',linewidth=2)
    plt.xlabel("Month")
    plt.ylabel("Dollar Amount ($)")
    plt.title("Expense per month")

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    ax1.pie(percentage, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, rotatelabels=True)

    ax1.axis('equal')

    Expenses_Breakdown_Table = pd.pivot_table(df1, values = ['Total Amount'], index = ['Category', 'Month_year'], aggfunc=sum).reset_index()
    Expenses_Breakdown_Table.columns = [x.upper() for x in Expenses_Breakdown_Table.columns]
    Expenses_Breakdown_Chart = px.line(Expenses_Breakdown_Table, x='MONTH_YEAR', y="TOTAL AMOUNT", title="Expenses Breakdown", color = 'CATEGORY')
    Expenses_Breakdown_Chart.update_yaxes(title='Expenses', visible=True, showticklabels=True)
    Expenses_Breakdown_Chart.update_xaxes(title='Date', visible=True, showticklabels=True)

    x = np.arange(len(df2["Month_Year"].tolist()))
    width = 0.35

    rects1 = ax2.bar(x - width/2, df2['amount'].tolist(), width, label='Spent',color='red')
    rects2 = ax2.bar(x + width/2, df3['amount'].tolist(), width, label='Income',color='green')

# Add some text for labels, title and custom x-axis tick labels, etc.
    ax2.set_ylabel('Dollars Spent ($)')
    ax2.set_title('Monthly Income vs Expenses')
    ax2.set_xticks(x)
    ax2.set_xticklabels(df2["Month_Year"].tolist())
    ax2.legend()

    fig2.tight_layout()

    Expenses_Breakdown_Chart.show()
    plt.show()

writeDataToCSV()