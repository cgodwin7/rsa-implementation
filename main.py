#!/usr/bin/python

"""
The Main script fetches user input flags "password", "file", and "gui" as
options then converts the "password" into Unicode integers. These integers
are encrypted, then loaded into a file. Upon decryption, the file is read
and then the integers are decrypted. After this step, the integers are converted
back into ASCII characters and the "password" is displayed to the user.
"""

import argparse
import pickle
import socket
import guitest as graphics

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--password", help="Password to encrypt", type=str, required=True)
    parser.add_argument("-f", "--file", help="Output File", type=str)
    parser.add_argument("-gui", "--gui", help="Enable GUI", action="store_true")
    try:
        args = parser.parse_args()
        if args.gui:
            graphics.GUI()
        from backend import crypt
    except Exception as e:
        print("Failure. Error: %s", e)

    message = args.password
    message = [ord(c) for c in message]
    enc_mess = []
    dec_mess = []
    for val in range(len(message)):
        enc_mess.append(crypt.encrypt(message[val]))
    if args.file:
        with open(args.file, 'wb') as fp:
            pickle.dump(enc_mess, fp)

	#print("Encrypted value:", enc_mess)
        with open(args.file, 'rb') as rb:
            test_mess = pickle.load(rb)

        for val in range(len(test_mess)):
            dec_mess.append(crypt.decrypt(test_mess[val]))
    else:
        for val in range(len(enc_mess)):
            dec_mess.append(crypt.decrypt(enc_mess[val]))
    dec_mess = [chr(c) for c in dec_mess]
    dec_mess = ''.join(dec_mess)
    print("Decrypted Message: " + dec_mess)

if __name__ == '__main__':
    main()
