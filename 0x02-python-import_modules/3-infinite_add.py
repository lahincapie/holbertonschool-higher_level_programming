#!/usr/bin/python3
import sys
#lista de argumentos
#convertirla en enteros
#sumar los argumentos 15 16 = 31

def main():
    list_arguments = sys.argv
    sum = 0
    for count in range(1, len(list_arguments)):
        sum += int(list_arguments[count])
    print("{}".format(sum))

if __name__ == "__main__":
    main()
