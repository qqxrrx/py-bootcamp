# generators are like list comprehension but uses () instead of []
# generators are forward only, once you read the item, you will not see it again
# generators are more lightweight than lists (need the least memory)
# if only iterating only once, use generators

import sys
list_comprehension = sys.getsizeof([x*10 for x in range(1000)])
generator_expression = sys.getsizeof(x*10 for x in range(1000))

print("comparisons: ")
print(f"list comprension: {list_comprehension} bytes")
print(f"generator expresison: {generator_expression} bytes")
