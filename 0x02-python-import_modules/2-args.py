#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = len(sys.argv) - 1

    if argument == 0:
        print("{} arguments.".format(argument))
    elif argument == 1:
        print("{} argument:".format(argument))
    else:
        print("{} arguments:".format(argument))


    if argument >= 1:
        argument = 0
        for arg in sys.argv:
            if argument != 0:
                print("{}: {}".format(argument, arg))
            argument += 1
