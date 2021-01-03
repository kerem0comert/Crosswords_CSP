from tabulate import tabulate


table = [["a","b","c"],["d","e","f"],["g","h","i"]]
print(tabulate(table,tablefmt="grid"))