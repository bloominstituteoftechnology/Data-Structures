# Print out each element of the following array on a separate line:

# a = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006", ['another', 'list']]

# You may use whatever programming language you'd like. Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

def print_lines():
    for i in a:
        if type(i) == str:
            print(i)
        
    for x in a[-1]:
            print(x)

print_lines()



# def black_jack():
#     a = [2, 3, 4, 5]
#     i = sum(a)
#     print(i)
#     # return i
#     if i > 21:
#         print(True)
#         return True        
#     else:
#         print(False)
#         return False        

# black_jack()
