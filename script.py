import sys

def foo(a, b):
    print("Tutaj jest wpisany pierwszy argument: {}".format(a))
    print("Tutaj jest wpisany drugi argument: {}".format(b))
    

if __name__ == "__main__":
    foo(*sys.argv[1:])