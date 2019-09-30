#!/usr/bin/env python3

# Created by: Mariam Hemdan
# Created on: Sep 2019
# This program calculates the circumference of a circle
#    with user input

import constants


def main():
    # This function calculates circumference

    # input
    radius = int(input("Enter radius of a circle (mm): "))

    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("circumference is {}mm^2".format(circumference))


if __name__ == '__main__':
    main()
