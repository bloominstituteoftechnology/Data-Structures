
ar = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
def rec(val):
    
    if len(val) == 0:
        return
    if val[0] % 3 == 0:
        
        print(val[0])
        #slice    
    return rec(val[1:])



rec(ar)
print(ar, "Variables")