# constant time
# the efficiency does not depend on the size of the input


# linear time
# the efficiency does depend on the time of the input
# iterates over every element in the list or a dict
for i in range(1000):
    print(i)


d = {
    "a": 'dog',
    'b': 'cat'
}

print(d.values(1))