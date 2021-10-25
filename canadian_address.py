#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program edits your address
#   with user input


def full_address(
    full_name, street_number, street_name, city, province, postal, apt_number=None
):
    # return the full formal name

    full_address = full_name
    if apt_number is not None:
        full_address = (
            full_address + "\n" + apt_number + "-" + street_number + " " + street_name
        )
    else:
        full_address = full_address + "\n" + street_number + " " + street_name
    full_address = full_address + "\n" + city + " " + province + " " + postal

    return full_address


def main():
    # gets a users name and prints out their formal name
    apt_number = None

    full_name = input("Enter your full name: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter your apartment number: ")
    city = input("Enter your city: ")
    province = input("Enter your province (ex; ON, BC..): ")
    postal = input("Enter your postal code (ex; K2A 123): ")

    try:
        street_number_int = int(street_number)

        if apt_number != None:
            location = full_address(
                full_name,
                street_number,
                street_name,
                city,
                province,
                postal,
                apt_number,
            )

        else:
            location = full_address(
                full_name, street_number, street_name, city, province, postal
            )

        print("")
        print(location.upper())

    except Exception:
        print("")
        print("Insert street number correctly and try again.")


if __name__ == "__main__":
    main()
