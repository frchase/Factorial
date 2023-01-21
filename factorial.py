def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))

#start factorial at 2 and increase as you go 
initial = 2
#this is our factorial num that we are going to compare
num = 0
#this will be our answer for factorial 
count = 0
#comparison for the different inputs (1 second, 10 minutes, etc..) and change this to solve for each
compare = 6E8
#this is just to store all of the results from factorial. The final number added will be over the comparison 
list = []

while num < compare:
    num = factorial(initial)
    count += 1
    initial += 1
    list.append(num)

print(count)
print(list)
