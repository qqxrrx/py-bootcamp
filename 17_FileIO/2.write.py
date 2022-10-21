# .write() overwrites everything when we are using mode='w'
with open("file2.txt", mode='w') as f:
    f.write("hello python\n")
    f.write("this is a new line\n")
    f.write("ok bye")
