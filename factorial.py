#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Nov 2022
# This program finds factorial of a number using while loop


def main():
    # this function finds factorial of a number using while loop

    # input
    num_as_string = input("Enter a number to find factorial: ")
    print("")

    # variables
    factorial = 1
    loop_counter = 0

    # process & output
    try:
        num = int(num_as_string)
        if num >= 0:
            while loop_counter < num:
                loop_counter = loop_counter + 1
                factorial = factorial * loop_counter
            print("{0}! = {1}.".format(num, factorial))
        else:
            print("{0}is not a positive integer.".format(num))
    except ValueError:
        print("{0} is not an integer".format(num_as_string))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
