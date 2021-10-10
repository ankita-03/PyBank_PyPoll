import csv

with open('Resources/budget_data.csv') as open_csv:
    csv_reader = csv.reader(open_csv)

    months = 0  # the months in budget_data.csv
    column = []  # the profit/losses column B in budget_data.csv
    net_total = 0 # net total of profitt/losses over a period
    previous_month = 0
    change_in_month = []
    #total_profit = 0
    dates = []

    next(csv_reader)

    for row in csv_reader:

        months += 1

        column.append(row[1])
        net_total = net_total + int(row[1])

        next_month = int(row[1])
        change = next_month - previous_month
        change_in_month.append(change)
        previous_month = next_month 

        # add dates into exisitng list
        dates.append(row[0])
        inc_profit = max (change_in_month)
        inc_date = dates[change_in_month.index(inc_profit)]

        dec_profit = min (change_in_month)
        dec_date = dates[change_in_month.index(dec_profit)]


x  = sum(change_in_month[1:])
y = len(change_in_month) - 1
avg_change = x/y
output = (f'''
Financial Analysis
  ----------------------------
  Total Months: {months}
  Total: ${net_total}
  Average  Change: ${avg_change}
  Greatest Increase in Profits: {inc_date} $({inc_profit})
  Greatest Decrease in Profits: {dec_date} $({dec_profit}) 
''')

print(output)