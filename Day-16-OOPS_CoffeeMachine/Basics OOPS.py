'''
Smaple program. We first download package and import class from it. Then we declare object and perform required operations.
'''

# Downloading packages in terminal or jupyter notebook
# pip install -U prettytable

# From the downloaded package,we import PrettyTable class
from prettytable import PrettyTable



# Object Creation
table = PrettyTable()
print(table)



# Adding Values in the table
table.field_names = ["Pokemon Name", "Type"]

table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])

# Alternate Way
table.add_column("Pokemon Name",["Pikachu","Squirtle", "Charmander"])
table.add_column("Pokemon Name",["Electric","Water", "Fire"])

# Printing the output
print(table)



# Changing the Alignment of our table
table.align = 'l'

# Printing the output
print(table)