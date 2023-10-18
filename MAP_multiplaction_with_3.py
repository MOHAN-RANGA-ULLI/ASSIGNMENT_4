# Write a Python program to triple all numbers of a given list of integers. Use Python map.



# sample list: [1, 2, 3, 4, 5, 6, 7]



# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]

# def fun(n):
#     return n*3


# l=eval(input('enter the list: '))

# x=list(map(fun , l))
# print(x)

l=[1, 2, 3, 4, 5, 6, 7]
x=list(map(lambda x: x*3 , l))
print(x)
