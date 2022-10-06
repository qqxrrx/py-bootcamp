def sum_odd_numbers(nums):
    total = 0
    for num in nums:
        if num % 2 != 0:
            total += num
    return total


print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))
