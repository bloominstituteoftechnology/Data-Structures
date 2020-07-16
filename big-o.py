"""
O(n) - Linear Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

# Constant, doesn't change computation
def print_animals(animal_list):
    for i in range(len(animal_list)):
        print(animal_list[i])


"""
What about this one? What runtime complexity is this one?
"""


def print_animals1(animal_list):
    for i in range(len(animal_list)): # O(n) - Linear
        print(animal_list[i]) # O(1)
        my_number = 0           # O(1)

        for _ in range(100000): # O(100_000) or O(1)
            my_number += 1      # O(1)

# Thus as a whole, # O(n * (1+1+1+ (100_000 *1))) = O(n * 100_003) ~= O(n)
#                    Outerloop * inner loop

"""
CFU: Slack Thread: Why doesn't the nested for loop make the time complexity O(n^2)?
"""


"""
O(n^2) & O(n^3) - Polynomial Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


# Print a list of all possible animal pairs
def print_animal_pairs(): # O(n * (n * 1) = O(n^2)
    for animal_1 in animals:
        for animal_2 in animals:
            print(f"{animal_1} - {animal_2}")


# Print a list of all possible animal triples
def print_animal_triples():
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")


# Print a list of all possible animal triples
def print_animal_triples1():
    for animal in animals:
        print(animal)

    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")


"""
CFU: Slack Thread
What's the time complexity to print all animal quintuples? What about "ten"tuples?
"""


"""
O(log n) - Logarithmic Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


# free all the animals, half at a time
# (remove them from the array)
def free_animals(animal_list):
    while len(animal_list) > 0:
        animal_list = animal_list[0: len(animal_list) // 2]

# We are reducing by half at each step
# This is the inverse of doubling at each step O(2^n) - Exponential Time


"""
CFU: Slack Thread
What's the worst the number of steps can get for a O(log n) time complexity
algorithm with an input size of 10 million?
"""

