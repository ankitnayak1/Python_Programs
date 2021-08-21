'''
Codebasics question 2 from Data Structures and Algorithms tutorial series
'''

'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

l = len(heros)

print("Length of heros =", + l)

# Adding black panther at the end of the list
heros.append('black panther')
print("Updated heros list =", heros)

# Adding black panther after hulk
heros.pop(5)
print("Updated heros list =", heros)
heros.insert(3, 'black panther')
print("Updated heros list =", heros)

heros[1:3] = ['doctor strange']
print("Updated heros list =", heros)

# Sorting the heros list
heros.sort()
print("Alphabetically sorted heros list =", heros)






