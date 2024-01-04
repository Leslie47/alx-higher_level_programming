#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argument = len(argv) - 1
    if argument < 1:
        print("{} arguments.".format(argument))
    elif argument == 1:
        print("{} argument:".format(argument))
    else:
        print("{} arguments".format(argument))
    for i in range(argument):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
