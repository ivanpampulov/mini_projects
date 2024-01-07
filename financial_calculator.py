'''
3. Better print out messages - give interest and final amount on separate lines
'''


class FinancialCalculator:

    def __init__(self, amount, rate, time):
        self.amount = amount
        self.rate = rate
        self.time = time

    def simple_interest(self):
        total = self.amount * (1 + self.rate * self.time)
        return f'{total:.2f}'

    def compound_interest(self):
        total = self.amount * (1 + self.rate / 1)**self.time
        return f'{total:.2f}'

    def loan_payment(self):
        total = self.amount * self.rate / 1 - (1 + self.rate) ** (-self.time)
        return f'{total:.2f}'

    def future_value(self):
        total = self.amount * (1 + self.rate) ** self.time
        return f'{total:.2f}'


def main_menu():
    print('Main Menu:')
    print(
        '1. Calculate Simple Interest \n'
        '2. Calculate Compound Interest\n'
        '3. Calculate Loan Payment\n'
        '4. Calculate Future Value of Savings\n'
        '5. Quit'
        )


main_menu()
command = input('Enter your choice (1/2/3/4/5): ')
while True:

    if command == '5':
        break

    amount = float(input('Enter amount: '))
    rate = (float(input('Enter rate per year: '))) / 100
    time = float(input('Enter period in years: '))

    if amount <= 0 or rate <= 0 or time <= 0:
        raise Exception('Sorry no numbers lower or equal to zero!')

    calculation = FinancialCalculator(amount, rate, time)

    if command == '1':
        print(f'{calculation.simple_interest()}')
    elif command == '2':
        print(f'{calculation.compound_interest()}')
    elif command == '3':
        print(f'{calculation.loan_payment()}')
    elif command == '4':
        print(f'{calculation.future_value()}')

    user_input = input('Would you like to do another calculation (y/n)?: ')

    if user_input == 'y':
        main_menu()
        command = input('Enter your choice (1/2/3/4/5): ')
    else:
        break

print('Goodbye!')