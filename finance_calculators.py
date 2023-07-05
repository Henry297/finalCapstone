import math  

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# accept a string input from the user
string_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# convert the string to uppercase using the upper() method
string_uppercase = string_input.upper()

# accept two string inputs from the user
string1 = "INVESTMENT" 
string2 = "BOND" 

# compare the two strings using the == operator
if string_uppercase == string1:
    print("You have selected INVESTMENT")
    P = float(input("Enter the amount of money that you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): "))
    t = float(input("Enter the number of years you plan on investing: "))
    string_interest = input("Enter the type of interest - “simple” or “compound” interest: ")
    string3 = "SIMPLE" 
    string4 = "COMPOUND" 

    # compare the two strings using the == operator
    if string_interest.upper() == string3:
        print("You have selected simple interest")
        A = P*(1 + (r/100)*t)
    elif string_interest.upper() == string4:
        print("You have selected compound interest")
        A = P * math.pow((1+(r/100)),t)

    print("The total amount of money applied to your interest is: ", A)

elif string_uppercase == string2:
    print("You have selected BOND")
    P = float(input("Enter the present value of the house: "))
    i = float(input("Enter the monthly interest rate, calculated by dividing the annual interest rate by 12. Remember to divide the interest entered by the user by 100 e.g. (8 / 100) before dividing by 12.: ")) 
    n = float(input("Enter the number of months over which the bond will be repaid: ")) 
    i = i/100
    repayment = (i * P)/(1 - (1 + i)**(-n))

    print("The amount of money you will have to repay each month is: ", repayment)

else:
    print("re-enter")

