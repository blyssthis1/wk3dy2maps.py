# Exercise #1
# Filter out all of the empty strings from the list below
# Output: ['Argentina', 'San Diego', 'Boston', 'New York']
#Answer:

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
print(list(filter(lambda num: num.strip() !=(""),places)))

#Excercise #2

#Answer:
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
x = sorted(author, key=lambda name: name.split(" ")[-1].lower())
print(x)



# Excercise #3

#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# F = (9/5)*C + 32

#Answer:
places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]
newplaces = list(map(lambda x: (x[0], (9/5) * x[1]+ 32), places))
print(newplaces)

# Exercise #4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.

# Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8


#Answer:
def fib(num):
    if num <= 1:
        return 1
    return fib(num-1) + fib(num-2)
fib(5)

print(fib(5))
