import numpy as np

def get_input():
    array = input("Enter a list of integers separated by spaces: ").split()
    return np.array(array, dtype=int)

def ufunc_product(arr):
    return np.prod(arr)

def ufunc_differences(arr):
    return np.diff(arr)

def lcm(a, b):
    return abs(a * b) // np.gcd(a, b)

lcm_ufunc = np.frompyfunc(lcm, 2, 1)

def ufunc_lcm(arr):
    result = arr[0]
    for num in arr[1:]:
        result = lcm_ufunc(result, num)
    return result

def ufunc_gcd(arr):
    return np.gcd.reduce(arr)

def main():
    arr = get_input()
    
    product_result = ufunc_product(arr)
    difference_result = ufunc_differences(arr)
    lcm_result = ufunc_lcm(arr)
    gcd_result = ufunc_gcd(arr)
    
    print(f"Product of elements: {product_result}")
    print(f"Differences between elements: {difference_result}")
    print(f"LCM of elements: {lcm_result}")
    print(f"GCD of elements: {gcd_result}")

if __name__ == "__main__":
    main()
