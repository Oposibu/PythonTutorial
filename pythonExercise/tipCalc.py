PriceOfMeal = eval(input('ENter the price of meal: '))
PercentageOfTip = eval(input('Enter the percentage of tips: '))
tips = (PercentageOfTip/100) * PriceOfMeal
bill = PriceOfMeal + tips
print('Amount of tip is: ', tips)
print('Your bill is: ', bill)
