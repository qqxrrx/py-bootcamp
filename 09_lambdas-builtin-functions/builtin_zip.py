from xml.dom import minidom


print("\n.zip()")
l1 = [1, 2, 3, "a", "b", "c"]
l2 = [4, 5, 6, 0]
print(list(zip(l1, l2)))
print(dict(zip(l1, l2)))


tups = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e")]
print("\nusing tuple unpacking:")
print(tups)
print(list(zip(*tups)))


midterms = [88, 98, 97]
finals = [96, 86, 99]
students = ['A', 'B', 'C']
print("\ncreate dictionary with only high scores:")
print("using dictionary comprehension:")
print({t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)})
print("using .map() built in function (average grade calculation instead): ")
print(dict(zip(students, map(lambda p: (p[0]+p[1])/2, zip(midterms, finals)))))
