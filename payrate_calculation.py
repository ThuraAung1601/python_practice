# Program to calculate payment roll
employee_name = input("Enter employee's name:")
num_of_hr_per_week = eval(input("Enter number of hours worked in a week:"))
hourly_pay_rate = eval(input("Enter hourly pay rate:"))
federal_tax_withholding_rate = eval(input("Enter federal tax withholding rate:"))
state_tax_withholding_rate = eval(input("Enter state tax withholding rate:"))

gross_pay = num_of_hr_per_week * hourly_pay_rate

federal_tax_withholding = gross_pay * federal_tax_withholding_rate
state_tax_withholding = gross_pay * state_tax_withholding_rate
total_deduction = federal_tax_withholding + state_tax_withholding

net_pay = gross_pay - total_deduction

print("Employee Name:", employee_name)
print("Hours Worked:", num_of_hr_per_week)
print("Pay Rate: ${}".format(hourly_pay_rate))
print("Gross Pay: ${}".format(gross_pay) )
print("Deductions:")
# print("\tFederal Withholding (" + format(federal_tax_withholding_rate,"3.1%") + "): $" + format(federal_tax_withholding,"3.2f"))
print("\tFederal Withholding ({}): ${}".format(format(federal_tax_withholding_rate,"3.1%"),format(federal_tax_withholding,"3.2f")))
print("\tState Withholding ({}): ${}".format(format(state_tax_withholding_rate,"3.1%"),format(state_tax_withholding,"3.2f")))
print("\tTotal Deduction: ${}".format(format(total_deduction,"3.2f")))
print("Net Pay: ${}".format(format(net_pay,"3.2f")))