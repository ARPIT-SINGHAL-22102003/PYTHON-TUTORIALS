#question 1

# def caluculate_area(height, base):
#     area = (1/2)*height*base
#     return area

# height = int(input("Enter the height: "))
# base = int(input("Ente the base: "))
# area_of_triangle = caluculate_area(height, base)
# print(area_of_triangle)

# print("------------------------------------------")

#question 2

# def caluculate_area(shape,height, base):
#     if(shape == "rectangle"):
#         area = height * base
#     elif(shape == "triangle"):
#         area = (1/2)*height*base
#     else:
#         area = (1/2)*height*base

#     return area

# height = int(input("Enter the height: "))
# base = int(input("Ente the base: "))
# shape = input("Enter the shape: ")
# area_of_shape = caluculate_area(shape, height, base)
# print(area_of_shape)

print("------------------------------------------")

#question 4

def pattern(n):
    for i in range(n+1):
        s = " "
        for j in range(i):
            s += "*"
        print(s)

n = int(input("Enter the value of n: "))
pattern(n)