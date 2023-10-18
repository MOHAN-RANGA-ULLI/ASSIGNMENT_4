# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]



def square(n):
    return n**2

l = [4,5,2,9]
x= list(map(square , l))
print(x)



# BY USING LAMBDA FUNCTION

# l = [4,5,2,9]
# x = list(map(lambda n: n**2 , l))
# print(x)