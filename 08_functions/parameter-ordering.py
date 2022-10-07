def correct_function_order(first_name, last_name, *args, default_text="yo", **kwargs):
    print(f"you are {first_name} {last_name}")
    print("your passed arguments were:")
    for arg in args:
        print(arg)
    print(f"default text was {default_text}")
    print("kwargs are:")
    for k, v in kwargs.items():
        print(f"{k} = {v}")


correct_function_order("john", "doe", move="jump", change="duck")
