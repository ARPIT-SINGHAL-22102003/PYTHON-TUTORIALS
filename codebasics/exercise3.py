# # Question 1
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# count = 0
# for i in result:
#     if(i == 'heads'):
#         count += 1
# print(count)


# print("------------------------------------------")


# #question 2
# for i in range(11):
#     if(i%2==1):
#         print(i*i)

# print("------------------------------------------")

# #question 3

# months = ["Jan", "Feb", "Mar", "Apr", "May"]
# expense_list = [2340, 2500, 2100, 3100, 2980]

# amount = int(input("Enter the expense: "))

# month = -1

# for i in range(len(expense_list)):
#     if amount == expense_list[i]:
#         month = i 
#         break
# if month != -1:
#     print(f"you spent this amount in {months[month]}")
# else:
#     print(f"You didn\'t spend this amount")

# print("------------------------------------------")

# #question 4

# for i in range(5):
#     print(f"You ran {i+1} miles") # i starts with zero hence adding 1
#     tired = input("Are you tired? ")
#     if tired == 'yes':
#         break

# if i == 4: # 4 because the index starts from 0
#     print("Hurray! You are a rock star! You just finished 5 km race!")
# else:
#     print(f"You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

print("------------------------------------------")

#question 5

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)