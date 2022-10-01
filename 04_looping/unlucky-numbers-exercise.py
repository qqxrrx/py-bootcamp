for i in range(1, 21):
    state = ""
    if i == 4 or i == 13:
        state = "UNLUCKY!"
    else:
        if i % 2 == 0:
            state = "even"
        else:
            state = "odd"
    print(f"{i} is {state}")
