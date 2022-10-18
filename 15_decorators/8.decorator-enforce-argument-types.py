# decorator to change argument types
def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            # zip() = ((arg1, type1), (arg2, type2))
            for (a, t) in zip(args, types):
                # casting = type1(arg1), type2(arg2)
                newargs.append(t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


repeat_msg(444, "3")


@enforce(float, float)
def divide(a, b):
    print(a/b)


divide("55", "42")
