# Recursive function - function that calls itself
# Have 2 Cases
# 1) Base (stopping)
# 2) Recursive (when function calls itself)




# Given Base and n that are both 1 or more, compute recursively
# (no loops) the value of the base to the n power, so powerN(3,2)
# is 9 (3 squared).

# from https://codingbad.com/prob/p158888

def powerN(base, n):
    # base case
    if n == 0:
        return 1
    elif n == 1:
        return base

    # recursive
    else:
        return base * powerN(base, n-1)


print(powerN(3, 1)) # 3
print(powerN(3, 2)) # 9
print(powerN(3,3)) # 27


# Given a string, compute recursively (no loops) the number of
# lowercase 'x' chars in the string.
# from https://codingbat.com/prob/p170371

def countX(str):
    # base case
    if len(str) == 0:
        return 0

    # recursive case
    else:
        # we found an x
        if str[0] == "x":
            return 1 + countX(str[1:])
        # we didn't find an "x"
        else:
            return countX(str[1:])

print(countX("xxhixx")) # 4
print(countX("xhixhix")) # 3
print(countX("hi")) # 0
