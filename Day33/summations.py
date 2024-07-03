import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

print("Original arrays:")
print(f"Array1: {arr1}")
print(f"Array2: {arr2}\n")

addArr = np.add(arr1, arr2)
print("Addition of the arrays:")
print(addArr)

sumArr = np.sum([arr1, arr2])
print("\nSummation of the arrays:")
print(sumArr)

sumAxisArr = np.sum([arr1, arr2], axis=1)
print("\nSummation of the arrays along the first axis:")
print(sumAxisArr)

cumSumArr = np.cumsum([arr1, arr2])
print("\nCumulative summation of the arrays:")
print(cumSumArr)

cumProdArr = np.cumprod([arr1, arr2])
print("\nCumulative product of the arrays:")
print(cumProdArr)

# if i save 1 rupee on the first day, 2 rupees on the second day, 4 rupees on the third day, and so on, how much money will i have saved in 30 days?
days = np.arange(1,31)
money = 2**days
print("\nMoney saved each day:")
print(money)
totalMoney = np.sum(money)
print("\nTotal money saved in 30 days:")
print(totalMoney)
