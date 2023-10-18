# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.



# sample input: 10

# sample output: 35

lambda_fun = lambda x : x+25

input_number = int(input('enter number:'))
x= lambda_fun(input_number)

print(f'the input is {input_number}')
print(f'the output is { x }')