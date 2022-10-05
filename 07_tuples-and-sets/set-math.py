print("\nset union using |")
s1 = {"a", "b", "c", "d"}
s2 = {"e", "f", "g", "h"}
print("combines two sets")
s_final = s1 | s2
print(s_final)


print("\nset intersection using &")
s1 = {"1", "2", "3", "4"}
s2 = {"5", "1", "7", "3"}
print("retrieve only those that exist on both sets")
s_final = s1 & s2
print(s_final)
