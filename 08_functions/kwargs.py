def fave_colors(**kwargs):
    print(kwargs)

    for k, v in kwargs.items():
        print(f"{k}'s number is {v}")


fave_colors(A=321, B=412, C=551, D=4125)
