import imp
from math import ceil, floor
# this will import ceil and floor only

from math import *


# Using * (asterix) import all the functions from
# the module (math in this case)

# Round off Function

print(math.ceil(2.5)) # Output-> 3

print(math.floor(2.5)) # Output -> 2

# Some basic mathematics calculation

print(math.sqrt(25)) # Output -> 5.0

print(math.factorial(5)) # Output -> 120 {Factorial of 5}

print(math.comb(5,2)) # nCr (combination) 5C2 -> 10

print(math.fsum([1,2,3,4,5,6,7,8,9,10]))
# Output -> Sum of the elements of the list 

print(math.gcd(20,24)) 
# Output-> GCD of 20 and 24

print(math.lcm(10,20))
# Output-> LCM of 10 and 20

# Power and logarithmic functions

print(math.exp(1))
# Output-> e^1

print(math.log(x, base))
# Output-> calculated as log(x)/log(base)

print(math.log2(8))
# Output calculated s log8 base 2 -> 3

print(math.log10(10))
# Output calculated s log8 base 10 -> 1

print(math.pow(2, 5))
# Output as 2 raised to power 5


# Trigonometric functions

# argument value in radians

print(math.sin(x)) 
# Return the sine of x radians


print(math.cos(x))
# Return the cosine of x radian


print(math.tan(x))
# Return the tangent of x radians


print(math.acos(x))
# Return the inverse of cosine of x, in radians


print(math.asin(x))
# Return the inverse of sine of x, in radians


print(math.atan(x))
# Return the inverse of tangent of x, in radians


# Angular conversion

print(math.degrees(x))
# Convert angle x from radians to degrees.


print(math.radians(x))
# Convert angle x from degrees to radians


# Hyperbolic functions

print(math.acosh(x))
# Return the inverse hyperbolic cosine of x


print(math.asinh(x))
# Return the inverse hyperbolic sine of x


print(math.atanh(x))
# Return the inverse hyperbolic tangent of x


print(math.cosh(x))
# Return the hyperbolic cosine of x


print(math.sinh(x))
# Return the hyperbolic sine of x


print(math.tanh(x))
# Return the hyperbolic tangent of x


# Constants

print(math.pi)
# The mathematical constant π = 3.14159 


print(math.e)
# The mathematical constant e = 2.71828 


print(math.tau)
# The mathematical constant τ = 6.283185
