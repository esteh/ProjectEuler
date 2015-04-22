#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
def ispythagorean(a,b,c):
    return a**2 + b**2 == c**2

for a in range(1,999):
    for b in range(1, 999):
        if ispythagorean(a,b,1000-b-a): 
            print a*b*(1000-b-a) 
#31875000
#a=200;b=375;c=425