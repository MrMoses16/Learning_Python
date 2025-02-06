# stores Persons info
class Person():
    def __init__(self, firstname = 'Kris', lastname = 'Tellez'):
        self.firstname = firstname
        self.lastname = lastname

class Financials():
    def __init__(self, income = 20000, expenses = 15000, other_income = 2000, other_expenses = 3000):
        self.other_income = other_income
        self.other_expenses = other_expenses
        self.income = income
        self.expenses = expenses
        
        
class PersonAccount(Person, Financials):
    def __init__(self, firstname='Kris', lastname='Tellez', income=20000, expenses=15000, other_income = 2000, other_expenses = 3000):
        Person.__init__(self, firstname, lastname)
        Financials.__init__(self, income, expenses, other_income, other_expenses)
        
    def total_income(self):
        return self.income + self.other_income
    
    def total_expenses(self):
        return self.expenses + self.other_expenses
    
    def net_worth(self):
        return self.income + self.other_income - (self.expenses + self.other_expenses)
    
    def info(self):
        return f'My name is {self.firstname} {self.lastname}. My total income is {PA.total_income()} and my total expenses are {PA.total_expenses()}. My net worth is {PA.net_worth()}.'
    
PA = PersonAccount()
print(PA.info())