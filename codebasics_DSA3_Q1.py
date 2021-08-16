'''Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
dct = {"January" : 2200,
       "February" : 2350,
       "March" : 2600,
       "April" : 2130,
       "May" : 2190}

extra_money = dct["February"] - dct["January"]
print("Extra money spent = ", + extra_money)

total_expenses = dct["January"] + dct["February"] + dct["March"]
print("Total expenses = ", + total_expenses)

# To see if we have spent more than Rs 2000 
if (dct["January"] == 2000):
    print("Yes it was spent in January")

elif (dct["February"] == 2000):
    print("Yes spent it in February")

elif (dct["March"] == 2000):
    print("Yes spent in March")

elif (dct["April"] == 2000):
    print("Yes spent it in April")

elif (dct["May"] == 2000):
    print("Yes it was spent in May")
    
else:
    print("Money was not spent above Rs 2000 in any month")
    
# Adding $ 1980 to June

dct.update({"June" : 1980})
print(dct)

# Adjusting $ 200 refund in the month of April
dct["April"] = dct["April"] - 200
print("Total amount spent after considering refund = ", dct["April"])
