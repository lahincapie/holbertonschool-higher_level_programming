#!/usr/bin/python3
""" entrada del programa """
# from <nombre del modulo> import <nombre de la funcion>
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
