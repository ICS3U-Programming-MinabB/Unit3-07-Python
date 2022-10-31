#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: Oct 24, 2022
# This program runs a dating game


def main():
    #get user age
    print("welcome to my dating simulator")
    user_input_as_string = int(input("enter your age : "))

    # a try catch
    try:
        # convert the string into an integer
        user_input_as_integer = int(user_input_as_string)
       
        #if statement
        if user_input_as_string < 25:
            print("you are too young")
        elif user_input_as_string >= 25 and user_input_as_string < 40:
            print("you can date my granddaughter")
        elif user_input_as_string > 40:
            print("you are too old")
        else:
            print("this is not a real age")

    except ValueError:
        print("please input an integer")
    finally:
        print("thank you for playing")
    


if __name__ == "__main__":
    main()