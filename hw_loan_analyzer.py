


from importlib.resources import path


loan_costs = [500, 600, 200, 1000, 450]
total_number_of_loans = len(loan_costs)
print("total number of loans in the list is", total_number_of_loans)

numbers = [500, 600, 200, 1000, 450]
Sum = sum(numbers)
print(Sum)



loan_amounts = [500, 600, 200, 1000, 450]
average = sum(loan_amounts) / len(loan_amounts)
print("The average loan price is $" + str(round(average, 2)))




# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "holding_months": 9,
    "hurdle_rate":0.20,
    "future_value": 1000,
}

#Step One identify the four parts - loan_price, Future_value, hurdle_rate, and holding_months
loan_price = 500  # Investment cost
future_value = 1000  # Future Value of the home
hurdle_rate = 0.20  # 0.20 = 20% # Annual Discount Rate; minimum return expected
holding_months = 9  # Number of months until sold (until Future Value)

#Step Two use the formula below to print the answer 
# present_value = ( "future_value")/(1+"annual_hurdle_rate"/12)** "remaining_months"
# print(f"Present Value is ${present_value}")
present_value = future_value/ (1 + (hurdle_rate / 12)) ** holding_months
print(f"Present Value is ${present_value}")





# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.



# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months




# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

#Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
# a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

loan_price = 500.00
present_value = 861.00
if present_value  >= loan_price:
         print(f"the loan is worth it")
elif present_value < loan_price:
        print(f"existing profit is not worth it")



 # Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.



# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
#Step One 
#How To Create Variable and List 

inexpensive_loans = [700,500,200,900]
print (inexpensive_loans)

#Step Two - List Indexing from smallest to largest 
loan_price = inexpensive_loans[2]
print(loan_price)

loan_price = inexpensive_loans[1]
print(loan_price)

loan_price = inexpensive_loans[0]
print(loan_price)


loan_price = inexpensive_loans[3]
print(loan_price)

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
#Step Three
#For Loop  Inside the for loop, write
#  an if-statement to determine 
# if the loan_price is less than or equal to 500
# only one variable is used on for loops!!!!!

inexpensive_loans = [700,500,200,900]
for x in inexpensive_loans:
    print(inexpensive_loans)

#Step Four 
# b. If the loan_price is less than or equal to 500 
# then append that loan to the `inexpensive_loans` list
#3. Print the list of inexpensive_loans.

#Here there are two variable, inexpensive_loans and loan_price, 
#this is used as apart of the statement to test if the 
#inexpensive_loans are less than the original loan price. 
#if the statement is true it is known as Bool 
#if the statement is false it is known as Boolean. 
inexpensive_loans = 500
loan_price = 200
if loan_price < inexpensive_loans:
         print(f" the loan price is less than or equal to 500 append to inexpensive list")

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
#Step Five 
#To add or update a list use the .append() method 
         inexpensive_loans = []
inexpensive_loans.append("500")
inexpensive_loans.append("200")
print(inexpensive_loans)



# @TODO: Print the `inexpensive_loans` list
inexpensive_loans = [200,500]
print (inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path

import pathlib
csvpath = pathlib.Path("inexpensive_loansabc.csv")
print(csvpath)

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.

import csv
with open('inexpensive_loansabc.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([200])
    writer.writerow([500])
    writer.writerow([700])
    writer.writerow([900])
