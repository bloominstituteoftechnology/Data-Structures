
# Iterative Function


def search(data, target):
    for n in data:
        if n == target: # <-- Stopping criteria is when we found the target, or didn't find the target.
            return True
        return False


l = ['1', '2', '3']


print(search(l, '1'))

# We need base cases aka stopping criteria. 
# How do we move closer to a base case?
# RECURSIVE Functionality
def recursive_search(data, target):
    if len(data) == 0:
        return False
    if data[-1] == target:
        return True
    return recursive_search(data[:-1], target)

print(recursive_search(l, '1'))
