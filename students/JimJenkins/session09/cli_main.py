#!/usr/bin/env python3

"""
Author: Jim Jenkins
Date: 12/10/2018

Description: menu for mail room.
"""

import sys
from textwrap3 import dedent
#from .mailroom import Donor, Donor_collection


def menu_selection():
    user_selection = input('Please indicate what you\'d like to do:\n'
                                  '1 - Send a Thank You\n'
                                  '2 - Create a Report\n'
                                  '3 - Send Letters to All Donors\n'
                                  '4 - Quit\n'
                                  'Selection: ')
    if user_selection is '1':
        thanks()
    elif user_selection is '2':
        create_report()
    elif user_selection is '3':
        write_letters_to_disk()
    else:
        exit()


def thanks():
    print('executing - thanks')


def create_report():
    print('executing - create_report')


def write_letters_to_disk():
    print('executing - write_letters_to_disk')


def quit():
    sys.exit()


selection_dict = {"1": thanks, "2": create_report, "3": write_letters_to_disk, "4": quit}


menu_selection()

# if __name__ == "__main__":
#  main()


#    donors = get_sample_donors()

#    prepare_to_run()

