class GrumpyDict(dict):
    # if you are not doing anything else and just inheriting, no need to create __init__()

    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f'YOU WANT "{key}"? IT DOES NOT EXIST.')

    def __setitem__(self, key, value):
        print("CHANGE DICTIONARY? DONE")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("NOT FOUND")
        return False


d = GrumpyDict({"first": "Tom", "animal": "cat"})
print(d)
d['wow']
d['first'] = "JOKE"
print(d)
print("first" in d)
