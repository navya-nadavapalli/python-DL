 
#CALCULATE EMI FOR CAR LOANS
#Defining Variables using data types
principal=float(input("Enter the loan Amount:"))
Annual_price=float(input("Enter the annual interest rate:"))
loan_years=int(input("Enter the loan in years:"))

#using operators and data types we need to calculate
#convert annual price to monthly price by using division operator
monthly_price = Annual_price/12/100  #according EMI formula
loan_months = loan_years*12  # convert the years in to months by multiplication operator

#we need to apply EMI formula
#by this we convert above declaration in to formula values
#apply according to variables
emi=(principal*monthly_price*(1+monthly_price)**loan_months)/((1+monthly_price)**loan_months-1)

#we need output to be like this
print(f"\nMonthly EMI to be paid: ₹{emi:.2f}")  # here we apply maps to get as pair values
                                            # f indicates formatted string