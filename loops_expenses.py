# expenses = [10.5, 8, 5, 9, 2, 3]
# total = sum(expenses)
# print("You spent $", total, " on lunch this week", sep="")
# for x in expenses:
#     sum = sum + x
#
#
# print("you spent $", sum, "on lunch this week", sep="")
# fruits = ["apple", "guava", "mango", "orange", "peach"]

# if "orange" in fruits:
#     print("yes, this fruit is in fruits")
# else:
#     print("blueberry is not part of fruits")
#
# for x in fruits:
#         print(x)

# print(fruits[1:])

# total = 0
# expenses = []
# for i in range(7):
#     expenses.append(float(input("Type in your expenses here \n")))
#
# total = sum(expenses)
# print("You spent N", total, " for the week of 29th April 2021", sep="")

total = 0
expenses = []
num_expenses = int(input("Enter number of expenses\n"))
for i in range(num_expenses):
    expenses.append(float(input("Type in your expenses here \n")))

total = sum(expenses)
print("You spent N", total, " for the week of 29th April 2021", sep="")

