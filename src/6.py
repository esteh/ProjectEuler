#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sumsquares = 0
squaresum = 0
for i in range(1, 10):
    sumsquares = sumsquares + pow(i, 2)
    squaresum = squaresum
    
print abs(pow(squaresum, 2)-sumsquares)
#285