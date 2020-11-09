# Script to calculate Demand
#sold   => total products sold (approx.)
#rev    => total reviews of the product
# taking corelation as 1 review per 100 products (ex. rev = 5 || sold = 500)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import date
from tabulate import tabulate

#Get the number of reviews per product
print("Enter how many reviews the product has: ")
rev = int(input())

#Factor which 1 review per f products sold
f = 100

#Calculate the approx. sold products
sold  = f*rev


#Get the price for the product
print("Please enter the price of the product: ")
p = float(input())

#Returns average about 10%
ret = (sold/10)
swr = sold - ret

print("Please enter your per product cost:")
cost = float(input())

print("Please enter your per product shipping cost:")
sc = float(input())

#Calculate total sales
sales = sold*p

#With Returns
tswr = swr*p

tc = (cost*sold)+(sc*sold)

profit = tswr - tc

print("")
today = date.today()
print("Date: "+ str(today))
print("")

per = (profit/tswr)*100

#Print data
print(tabulate([['Approximate qty sold', str(sold)],
                ['Total sales without returns', str(sales)],
                ['Average Returns', str(ret)],
                ['Total sales with returns', str(tswr)],
                ['Total costs', str(tc)],
                ['Profit to-date', str(profit), str(per)+' %' ]]
                , headers=['Statistics', '','Percentage'], tablefmt='orgtbl'))
