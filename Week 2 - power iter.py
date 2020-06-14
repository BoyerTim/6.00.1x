"""
Write an iterative function iterPower(base, exp) that calculates the exponential  base^exp  by simply using successive multiplication. 
For example, iterPower(base, exp) should compute  base^exp by multiplying base times itself exp times.

This function should take in two values - base can be a float or an integer; exp will be an integer  ≥  0. 
It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    
    y = base
    for i in range(exp-1):
        y *= base
    return y

print(iterPower(0.9, 3))
