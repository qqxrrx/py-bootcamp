nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(f"nested_list[0][1]: {nested_list[0][1]}")
print(f"nested_list[1][-1]: {nested_list[1][-1]}")
print(f"nested_list[-1][-2]: {nested_list[-1][-2]}")


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for l in nested_list:
    for val in l:
        print(val)


coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]
for loc in coords:
    for coord in loc:
        print(coord)


print("nested list comprehension:")
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
[[print(val) for val in l] for l in nested_list]


print("nested loop simplification, converted to nested list comprehension: ")
# parent will loop 3 times and each iteration the child will execute 3 times
board = [[child_ for child_ in range(1, 4)] for parent_ in range(1, 4)]
print(board)


print("nested list comprehension with conditional: ")
# parent will loop 3 times and each iteration the child will either print "X" if odd or "O" if even
print([["X" if num % 2 != 0 else "O" for num in range(1, 4)]
      for val in range(1, 4)])
