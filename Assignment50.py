'''Create a pie chart to visualize the distribution of your monthly income by source. You have collected data on the various sources of your income, such as salary, freelance work, investments, and rental income. Share your conclusion/analysis.

 Input: income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other'] 

monthly_income = [5000, 1500, 1000, 600, 400]'''


import matplotlib.pyplot as plt

#This is input Given
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']

#Given monthly_income
monthly_income = [5000, 1500, 1000, 600, 400]

#colours 
colours = ['red','yellow','lightgreen','lightblue', 'orange']

plt.pie(monthly_income, labels=income_sources, colors=colours)
plt.title('monthly income by source')

plt.show()

