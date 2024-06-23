from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Country Name", ["India", "China", "Nepal"])
table.add_column("Capital", ["Delhi", "Beijing", "Kathmandu"])

table.align = "l"
print(table)
