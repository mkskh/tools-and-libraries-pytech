from tabulate import tabulate


table = [
    ["Maksym", "Kharchenko", "0502404907"]
]

headers = ["Name", "Lastname", "Number"]

print(tabulate(table, headers=headers, tablefmt="pipe"))