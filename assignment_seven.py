#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: December 2019
# This program prints odd numbers in a range


def odd_number(x_value_list, y_value_list):
    # This function processes if a number is odd and outputs it

    # variables
    number_integer = 1

    # process & output
    z_value_list = x_value_list * y_value_list
    print("\n" "Odd Numbers from 1 to {}"
          .format(z_value_list))

    while number_integer <= z_value_list:
        if number_integer % 2 != 0:
            print("{}"
                  .format(number_integer))
            number_integer = number_integer + 1
        elif number_integer % 2 == 0:
            number_integer = number_integer + 1
        continue

    return odd_number


def main():
    # this function asks the user for values and calls a function

    # input
    print("This program will take the value of x and multiply it by y,\n"
          "  then find the odd numbers from 1 to z. ")
    try:
        x_value = int(input("\nEnter the positive integer value of x: "))
        y_value = int(input("\nEnter the positive integer value of y: "))

        # calling a function
        output_odd = odd_number(x_value, y_value)
    except ValueError:
        print("")
        print("Please insert a valid integer")


if __name__ == "__main__":
    main()
