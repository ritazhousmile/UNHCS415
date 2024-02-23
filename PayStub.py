# Rita Zhou
# 2_Pay stub Assignment
# 2/20/2024
from datetime import datetime

# reading input
full_name = input("Enter your Full Name: ")
anniversary_month: int = int(input("Enter your Anniversary Month(1-12): "))
anniversary_year: int = int(input("Enter your Anniversary Year: "))
hours_worked: int = int(input("Enter your hours worked this pay period(0-350): "))
job_title = input(" Enter your Job Title: ")
pay_rate: float = float(input("Enter your pay rate: "))


# calculations
# calculate months worked

def pay_period():
    today_month = datetime.today().month
    today_year = datetime.today().year
    return today_month, today_year


def _months_worked(start_year, start_month,pay_month, pay_year):
    # today_month = datetime.today().month
    # today_year = datetime.today().year

    month_worked = 0
    if start_year == pay_year and pay_month > start_month:
        month_worked = pay_month - start_month
    else:
        month_worked = (pay_year - start_year) * 12 + (pay_month - start_month)
    return month_worked


# calculate vacation hours Calculate the vacation hours earned this pay period as the number of months worked times
# the vacation rate of 8.25 vacation hours per month. Vacation hours are reported to two significant digits. For
# example, 0.12 or 12.79
def vacation_hours(months):
    vacation_rate = 8.25
    hours = months * vacation_rate
    format_hours = format(hours, ".2f")
    return format_hours


# calculate gross pay defined as the hours worked times pay rate.

def gross_pay(hours, rate):
    return hours * rate


# Calculate the retirement withholding for the employee, which is defined as the gross pay times the retirement rate
# of 5.2%. (i.e grossPay * .052)
def retirement_withholding(pay):
    rate = 5.2 / 100
    return pay * rate


# Calculate the tax withholding for the employee, which is defined as the taxable income (gross pay minus retirement
# withholding) times the tax rate of 28.0%.
def tax_withholding(pay, withholding):
    tax_rate = 28.0 / 100
    return (pay - withholding) * tax_rate


# Calculate the net pay which is gross pay minus retirement minus tax withholding's.

def net_pay(pay, retire, tax):
    return pay - retire - tax


payMonth = 2
payYear = 2023

months_worked = _months_worked(anniversary_year, anniversary_month, payMonth, payYear)
hours_earned = vacation_hours(months_worked)
grossPay = gross_pay(hours_worked, pay_rate)
retirement = retirement_withholding(grossPay)
tax = tax_withholding(grossPay, retirement)
netPay = net_pay(grossPay, retirement, tax)

# output

print("==========================================\n      Gekko & Co.\n")
print('          "$"\n          ~~~\n         /  \  `.')
print("        /   \  /")
print("       /___ \/")
print("--------------------------------------------")
print(f"Pay Period:         {payMonth}/{payYear}")
print(f"Name:               {full_name}")
print(f"Title:              {job_title}")
print(f"Hire Date:          {anniversary_month}/{anniversary_year}")
print(f"Months Worked:      {months_worked}")
print(f"Vacation hours:     {hours_earned} ")
print("--------------------------------------------")
print(f"Gross pay:          ${grossPay:.2f}")
print(f"Retirement:         ${retirement:.2f}")
print(f"Tax:                ${tax:.2f}")
print("------------------------")
print(f"Net Pay:            ${netPay:.2f}")
print("==========================================")
