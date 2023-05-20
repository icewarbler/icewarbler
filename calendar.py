import pip
pip.main(['install', 'requests'])

from tabulate import tabulate
 
# assign data
dates = [
    ["1", "2", "3", "4", "5", "6", "7"],
]
 
# create header
head = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
 
# display table
print(tabulate(dates, headers=head, tablefmt="grid"))
