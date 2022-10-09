import pkg1
import pkg2

print(pkg1.__name__)
print(pkg1.fn.__name__)
print(pkg1.other_fn.__name__)


def my_def():
    # execution context __name__ is always "__main__"
    print(f"name of main file running this is {__name__}")


my_def()
