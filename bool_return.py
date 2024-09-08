def is_larger(aa, bb):
    return aa > bb

def is_same(aa, bb):
    return aa == bb

def is_smaller(aa, bb):
    return aa < bb


a = 11
b = 41

if a > b:
    print("a is larger than b")
else:
    print("a is not larger than b")

print("a > b:", is_larger(a,b))    
print("a == b:", is_same(a,b))
print("a < b:", is_smaller(a,b))