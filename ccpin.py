#!/usr/bin/env python3
"""
Validates that information matches using valid_input
"""

def valid_input(user_pin):
    """
    Checks if input equals the pin number
    args:
        user_pin: the user typed pin
    return:
        true: user_pin matches correct_pin
        false: user_pin is wrong format or
                the wrong length
                or wrong set of numbers
    """
    correct_pin = "1234"

    if user_pin == correct_pin:
        print ("Correct PIN")
        return True
    elif len(user_pin) != len(correct_pin):
        print ("Incorrect PIN Length")
        return False
    elif user_pin.isdigit() != True:
        print ("Incorrect PIN format")
        return False
    else:
        print ("Incorrect PIN")
        return False


def main():
    """
    User enters in pin number
    Checks through valid_input if the pin is correct
    Correct: exit(0)
    Incorrect: loop starts again asking for accurate input
    Incorrect(3 times): card blocked and exit(1)
    """
    wrong = 0
    while wrong != 3:
        user_pin = input("Enter your PIN: ")
        if valid_input(user_pin):
            exit(0)
        else:
            wrong = wrong + 1
    if wrong == 3:
        print("Your bank card is blocked")
        exit(1)

if __name__ == "__main__":
    main()
    exit(0)
