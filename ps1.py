months_per_yr = 12.0
month = 0.0
# total_amount_paid = 0.0
#
# balance = float(raw_input('Enter the outstanding balance on your credit card: '))
# annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
# min_month_payment_rate = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))
#
# while month != months_per_yr :
#     month += 1.0
#
#     min_month_payment = round((min_month_payment_rate * balance), 2 )
#     # Minimum monthly payment = Minimum monthly payment rate x Balance
#     # (Minimum monthly payment gets split into interest paid and principal paid)
#     interest_paid = round((annual_interest_rate / months_per_yr * balance), 2 )
#     # Interest Paid = Annual interest rate / 12 months x Balance
#     principal_paid = min_month_payment - interest_paid
#     # Principal Paid = Minimum monthly payment - Interest Paid
#     remaining_balance = balance - principal_paid
#     # Remaining Balance = Balance - Principle Paid
#     total_amount_paid += min_month_payment
#
#     print 'Month: '+ str(int(month))
#     print 'Minimum monthly payment: $' + str(min_month_payment)
#     print 'Principal paid: $' + str(principal_paid)
#     print 'Remaining balance: $' + str(remaining_balance)
#
#     balance = remaining_balance
#     if month == months_per_yr :
#         print 'RESULT'
#         print 'Total amount paid: $' + str(total_amount_paid)
#         print 'Remaining balance: $' + str(remaining_balance)

balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annual_interest_rate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

minimum_monthly_payment = 10.0
monthly_interest_rate = annual_interest_rate / months_per_yr

