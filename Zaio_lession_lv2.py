# ---------------------------------------------------------
# PYTHON CHALLENGE: THE NET SALARY CALCULATOR (SARS 2026/27)
# ---------------------------------------------------------

# QUESTION 1: 
# Create three variables to get user input (floats):
monthly_gross_salary = float(input())
medical_aid_premium = float(input())
num_dependents = int(input()) #(for medical credits)


# QUESTION 2:
# Calculate the monthly UIF contribution. 
# Remember: It is 1% of gross salary, but it is capped at R177.12.
# Hint: Use an 'if' statement or the min() function.
UIF = float(monthly_gross_salary * 0.01)
if UIF > 177.12:
    print("UIF cap exceed")
else :
    print("UIF contribution is good")
    
# QUESTION 3:
# To calculate tax (PAYE), we need the annual salary.
# Create a variable 'annual_gross' by multiplying monthly salary by 12.
annual_salary = float(monthly_gross_salary * 12)
PAYE = float(annual_salary * 0.18)
print("Question 3: ", PAYE)

# QUESTION 4:
# Using the 2026/27 Tax Brackets, create an if/elif/else structure
# to calculate the 'base_tax' on the 'annual_gross'.
# Example: 
# If income <= 245100, tax is 18%.
# If income > 245100 and <= 383100, tax is 44118 + 26% of amount above 245100.
if  245101 <= annual_salary < 383099:
    base_tax = float((annual_salary * 0.26) - 44118)
    print("Question 4: Base Tax: R", base_tax)
else: 
    if 0 <= annual_salary <= 245100:
        base_tax = float(annual_salary * 0.18)
        print("Question 4: Base Tax: R", base_tax)

# QUESTION 5:
# Everyone gets a Primary Rebate of R17,820 per year.
# Subtract this rebate from your 'base_tax'. 
# Note: Tax cannot be less than zero!
rebate = float(17820)
rebate_tax = float(base_tax - rebate)

print("Question 5: Rebate: R", rebate_tax)


# QUESTION 6:
# Medical Tax Credits (MTC) reduce your tax.
# For 2026, the main member gets R376 off per month.
# Calculate the 'monthly_tax' by dividing annual tax by 12, 
# then subtract the R376 credit.
monthly_tax = float((base_tax / 12) - 376)

print("Question 6: Monthly_tax: R", monthly_tax)

# QUESTION 7:
# Final Step! Calculate the 'net_salary'.
# Formula: Gross - Monthly Tax - UIF - Medical Aid Premium.
monthly_net = float(monthly_gross_salary - (monthly_tax + UIF + medical_aid_premium))
print("Question 7: Net Salary: R", monthly_net)

# QUESTION 8:
# Print a professional payslip showing:
# Gross Salary, UIF Deduction, Tax Paid, and the final Net Salary.
print("Gross Salary: R", monthly_gross_salary)
print("UIF Deduction: R", UIF)
print("Tax Paid: R", monthly_tax)
print("Net Salary: R",monthly_net)