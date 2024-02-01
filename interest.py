

# Constant months in a year
MONTHS_IN_A_YEAR = 12

# Assign the investment value to principal
print("Enter the principal value")
principal = float(input())

# Assign the correct value to rate (interest rate input)
print("Enter the interest rate")
interestRate = float(input())


# Calculate the interest
interestEarned = principal * interestRate

# Calculate the updated principal
updatedPrincipal = principal + interestEarned

#Output the calculated interest
print(f"The interest eared is ${interestEarned:.2f}")

# Output the updated principal value
print(f"The value of the investment after one year is ${updatedPrincipal:.2f}")

# Output calculate the average interest paid per month

print(f"The average interest is ${interestEarned / MONTHS_IN_A_YEAR:.2f}")
