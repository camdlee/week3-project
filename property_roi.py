# Topics from this week:
# RegEx - searching for patterns within texts, strings, files, etc - like filtering for email inputs
# Lambda, Map, Filter, Recursion, Generators - 
# In & Out of place algorithms, two pointers, linked lists, merge sort, 
# Time & Space complexity, Data structures - Arrays, stacks, queues, linked lists


# Assignment - Create a object oriented program that calculates Return on Investment for a property
# Scenario 
# Purchase price of house - 200,000


class Roi():
    def __init__(self, num_units, purchase_price):
        self.num_units = num_units
        self.purchase_price = purchase_price
        self.income_dict = {}
        self.total_monthly_income = 0
        self.expenses_dict = {}
        self.total_monthly_expenses = 0


#----------INCOME---------
    def income(self):
        print('---------MONTHLY INCOME CALCULATOR---------')
        while True:
            # ask user for income stream for each unit in the property
            income = input(f'Type in the Unit # and income generated by that unit [Unit, $]--(type "q" to quit)--: ')
            if income.lower() == 'q':
                break
            else:
                # we'll have to split this string and use 1st index as key and 2nd index as value
                #print(income.split(', '))
                unit_income = income.split(', ')
                self.income_dict[unit_income[0]] = unit_income[1]
                #print(self.income_dict)
        # print list of all the units and each income
        for key, value in self.income_dict.items():
            print(f'Unit {key} : ${value}')
        # calculate total monthly income from income dictionary
        for value in self.income_dict.values():
            self.total_monthly_income += int(value)
        print(f'Total monthly income: ${self.total_monthly_income}')
        

#-----Testing Code-----
# house = Roi(2,200000)
# house.income()

#----------EXPENSES---------
    def expenses(self):
        print('---------MONTHLY EXPENSES CALCULATOR---------')
        while True:
            # ask user for expense stream for each unit in the property
            expense = input(f'Type in the expense name and cost [Expense name, cost]--(type "q" to quit)--: ')
            if expense.lower() == 'q':
                break
            else:
                # we'll have to split this string and use 1st index as key and 2nd index as value
                #print(expense.split(', '))
                expense_cost = expense.split(', ')
                self.expenses_dict[expense_cost[0]] = expense_cost[1]
                #print(self.expenses_dict)
        # print list of all the units and each expense
        for key, value in self.expenses_dict.items():
            print(f'Unit {key} : ${value}')
        # calculate total monthly expenses from expenses dictionary
        for value in self.expenses_dict.values():
            self.total_monthly_expenses += int(value)
        print(f'Total monthly expenses: ${self.total_monthly_expenses}')

#-----Testing Code-----
# house = Roi(2,200000)
# house.expenses()


#---------CASH FLOW---------
# Dependent on Income and Expenses
# Monthly Cash flow = Income - Expenses
    def cash_flow(self):
        print('---------MONTHLY CASH FLOW---------')
        monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        print(f'Monthly cash flow: ${monthly_cash_flow}')


#---------CASH ON CASH ROI---------
# Dependent on how much money we put into the deal
    # Down payment, closing costs, renovation, mics.
# Total investment at time
# Annual Cash Flow = 12 * Monthly Cash Flow
# Annual Cash Flow / Total Investment = Return on Investment 