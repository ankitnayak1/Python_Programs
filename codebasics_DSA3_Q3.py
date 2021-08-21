'''
Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function
'''

# print("Enter the maximum number = ", end = ' ')
num = int(input("Enter the maximum number = "))

arr = []
for i in range(num):
    if (i%2 != 0):
        arr.append(i)

print("New list =", arr)