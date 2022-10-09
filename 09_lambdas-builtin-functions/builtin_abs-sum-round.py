print("\n.abs()")
print(f"abs(-44): {abs(-44)}")
print(f"abs(-424.124): {abs(-424.124)}")
# math.fabs = treat numbers as float first so an integer will be returned as a float


print("\n.sum()")
nums = [1, 23, 4, 5, 6, 6, 3]
print(sum(nums))
print(sum(nums, start=44))


print("\n.round()")
print(round(3.51, ndigits=5))
print(round(3.49))
