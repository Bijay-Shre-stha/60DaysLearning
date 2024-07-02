import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 9, 0, 7, 8])

# add
add = np.add(arr1, arr2)
print("Addition: ", add)

# subtract
subtract = np.subtract(arr2, arr1)
print("Subtraction: ", subtract)

# multiply
multiply = np.multiply(arr1, arr2)
print("Multiplication: ", multiply)

# divide
divide = np.divide(arr1, arr2)
print("Division: ", divide)

# power
power = np.power(arr1, 2)
print("Power: ", power)

# mod
mod = np.mod(arr2, arr1)
print("Modulus: ", mod)

# reciprocal
reciprocal = np.reciprocal(arr1)
print("Reciprocal: ", reciprocal)

# negative
negative = np.negative(arr1)
print("Negative: ", negative)

# absolute
absolute = np.absolute(negative)
print("Absolute: ", absolute)

# sign
sign = np.sign(arr1)
print("Sign: ", sign)

# greater
greater = np.greater(arr1, arr2)
print("Greater: ", greater)

# greater_equal
greater_equal = np.greater_equal(arr1, arr2)
print("Greater Equal: ", greater_equal)

# less
less = np.less(arr1, arr2)
print("Less: ", less)

# less_equal
less_equal = np.less_equal(arr1, arr2)
print("Less Equal: ", less_equal)

# equal
equal = np.equal(arr1, arr2)
print("Equal: ", equal)

# not_equal
not_equal = np.not_equal(arr1, arr2)
print("Not Equal: ", not_equal)

# logical_and
logical_and = np.logical_and(arr1, arr2)
print("Logical And: ", logical_and)

# logical_or
logical_or = np.logical_or(arr1, arr2)
print("Logical Or: ", logical_or)

# logical_xor
logical_xor = np.logical_xor(arr1, arr2)
print("Logical Xor: ", logical_xor)

# logical_not
logical_not = np.logical_not(arr1)
print("Logical Not: ", logical_not)

# maximum
maximum = np.maximum(arr1, arr2)
print("Maximum: ", maximum)

# minimum
minimum = np.minimum(arr1, arr2)
print("Minimum: ", minimum)

# fmax
fmax = np.fmax(arr1, arr2)
print("Fmax: ", fmax)

# fmin
fmin = np.fmin(arr1, arr2)
print("Fmin: ", fmin)

# isfinite
isfinite = np.isfinite(arr1)
print("Isfinite: ", isfinite)

# isinf
isinf = np.isinf(arr1)
print("Isinf: ", isinf)

# isnan
isnan = np.isnan(arr1)
print("Isnan: ", isnan)

