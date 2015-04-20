#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def ispalindrome(n):
    temp = str(n)
    return temp[0:len(temp)/2] == temp[len(temp):len(temp)/3:-1]
    
#print ispalindrome(906609)
maxx = 0
maxy = 0
for x in range(100, 999):
    for y in range(100, 999):
        n = y*x
        if ispalindrome(n):
            if maxx* maxy < n:
                maxx = x
                maxy = y
        
print maxx * maxy 
# 906609