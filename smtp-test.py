#!/usr/bin/env python3

import smtplib
import argparse
import sys
import getpass


def testmail(username, password, server, deliveryaddr):
    header = "From: %s\r\nTo: %s\r\nSubject: SMTP Test\r\n\r\nTest Successful" % (username, deliveryaddr)

    try:
        server = smtplib.SMTP(server)
        server.login(username, password)
        server.sendmail(username, deliveryaddr, header)
    except Exception as e:
        print("An Error Occurred! %s" % e)
    else:
        print("Test Successful")


def get_interactive_data():
    class Data():
        user = ''
        password = ''
        server = ''
        dest = ''

    data = Data()

    data.user = input("Username for SMTP Login: ")
    data.password = getpass.getpass("\nPassword for SMTP Login: ")
    data.server = input("\nSMTP Server URL: ")
    data.dest = input("\nDestination Email Address: ")

    return data

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', required=True,
                        help="Username for SMTP Login")
    parser.add_argument('-p', '--password', required=True,
                        help="Password for SMTP Login")
    parser.add_argument('-s', '--server', required=True,
                        help="SMTP Server URL")
    parser.add_argument('-d', '--dest', required=True,
                        help='Destination Email Address')

    if len(sys.argv) == 2 and sys.argv[1].lower() == '-i':
        args = get_interactive_data()
    else:
        args = parser.parse_args()

    testmail(args.user, args.password, args.server, args.dest)
