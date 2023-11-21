x = [12,89,34,22,67,24,46,91,59,97]

print("------------------------------------------------")
print(x[1])


# There are 2 types of indexing -------------->

# ● Positive indexing --> [left to right]
# ● Negative indexing --> it'll start from right side [right to left]

#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1   <----  -ve  

#    x = [12,89,34,22,67,24,46,91,59,97]

# +ve --> 0  1  2  3  4  5  6  7  8  9

# slice operator is used to get multiple elements in an array

#  start index : end index + 1

# if i want all the elements from 4th index to the 8th
# starting index : ending index+1 --->  [4 : 9]

print("------------------------------------------------")
print(x[4:])

# [start index : ] --> it will get all the elements starting from the start index 

print("------------------------------------------------")
# [:] --> will return everything!!
print(x[:])

print("------------------------------------------------")
# [:end index ] --> will return all the elements starting from the 0th index till the end index-1
print(x[:3])

#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1   <----  -ve  

#    x = [12,89,34,22,67,24,46,91,59,97]

print("------------------------------------------------")
print(x[-4:-1])

print("------------------------------------------------")
print(x[-8:-4])


print("------------------------------------------------")
print(x[-8 : ])


# ---------------------------------- FOR LOOP ---------------------------------------------------------

# print("---------------------------")
# for i in range(1,11):
#     print(i)

# print("---------------------------")
# for i in range(100, 116):
#     print(i)

# print("---------------------------")

# # range(starting num , ending num + 1 , step)
# for i in range(1 , 11 , 2):
#     print(i)

# print("---------------------------")
# for i in range(20, 41, 2):
#     print(i)

# print("---------------------------")
# # step is -ve (decrementing) in that case starting number > ending number
# for i in range(20, 11, -2):
#     print(i)

print("---------------------------")
# for i in range(50, 9, -5):
#     print(i)


x = [23,45,78,90]

for i in x:
    print(i)


# -----------------------------------------------------------------------------

marks = [75, 98, 89, 86, 79, 62, 78, 61, 90, 97, 92, 61, 64, 97, 82, 69, 87, 96, 65, 75, 85, 76, 95, 83, 62, 80, 80, 77, 94, 71, 86, 94, 85, 99, 77, 68, 92, 91, 99, 90]

occur = int(input("Enter the number you want to check the occurenece of: "))

occured = 0

for i in marks:
    if i == occur:
        occured += 1

print(occured)


