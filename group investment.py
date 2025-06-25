print('THE GROUP INVESTMENT STRATEGY PROJECT PROGRAM \n GOAL: TO ENABLE INVESTMENT POSSIBILITY FOR SMALL INCOME EARNERS \n ENCOURAGING FAIR AND TRUSTWORTHY SHARES AND \n PROFIT DISTRIBUTION AMONG SHAREHOLDERS AS TO MAINTAIN AND \n EXPAND TO INCREASE THE DAILY CASH FLOW OF THE CORE MEMBER')

invester1 = float(input('Enter the amount of money you like to join the investment team with: '))
invester2 = float(input('Enter the amount of money you like to join the investment team with: '))
invester3 = float(input('Enter the amount of money you like to join the investment team with: '))
invester4 = float(input('Enter the amount of money you like to join the investment team with: '))
invester5 = float(input('Enter the amount of money you like to join the investment team with: '))
invester6 = float(input('Enter the amount of money you like to join the investment team with: '))

Total_capital = invester1 + invester2 + invester3 + invester4 + invester5 + invester6
general_profit = float(input('Enter the general profit to be distributed to the investors: '))

print(f'The total capital from all the investors gives us a total of: {Total_capital}')

def calculate_profit(investment, total_capital, general_profit):
    profit_percentage = (investment / total_capital) * 100
    actual_profit = (profit_percentage / 100) * general_profit
    business_maintenance = 0.30 * actual_profit
    actual_profit_after_maintenance = actual_profit - business_maintenance
    return int(actual_profit), int(business_maintenance), int(actual_profit_after_maintenance)

profits = []
for i, investment in enumerate([invester1, invester2, invester3, invester4, invester5, invester6], start=1):
    actual_profit, business_maintenance, actual_profit_after_maintenance = calculate_profit(investment, Total_capital, general_profit)
    profits.append((actual_profit, business_maintenance, actual_profit_after_maintenance))
    print(f'The profit for investor {i} before maintenance is: {actual_profit}')
    print(f'The business maintenance cost for investor {i} is: {business_maintenance}')
    print(f'The profit for investor {i} after maintenance is: {actual_profit_after_maintenance}')