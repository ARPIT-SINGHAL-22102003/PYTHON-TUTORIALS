# question 1
# exp = [2200, 2350, 2600, 2130, 2190]
# print("I spent", exp[1]-exp[0],"dollars more in february as compared to january" )
# print("Expense in 1st quarter: ", exp[0]+exp[1]+exp[2])
# print(2000 in exp)
# exp.append("1980")
# print(exp)
# exp[3] = exp[3]-200
# print(exp)

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append("black panther")
print(heros)

heros.remove("black panther")
print(heros)
heros.insert(3, "balck panther")
print(heros)

heros[1:3] = ["doctor strange"]
print(heros)

heros.sort()
print(heros)