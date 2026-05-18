#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb = len(sys.argv) - 1
    if nb == 0:
        print("0 arguments.")
    elif nb == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nb))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
