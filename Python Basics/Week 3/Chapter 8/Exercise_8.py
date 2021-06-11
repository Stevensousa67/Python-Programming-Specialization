# Given the lengths of three sides of a triange, determine whether the triangle is right angled. If it is, the assign
# True to the variable is_rightangled. If it’s not, then assign False to the variable is_rightangled.
#
# Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for
# equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up
# as: if  abs(x - y) < 0.001:      # if x is approximately equal to y

a = 4
b = 3
c = 5

if a*a + b*b == c*c:
    is_rightangled = True
else:
    is_rightangled = False

print(is_rightangled)
