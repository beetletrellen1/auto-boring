#! python3
# pw.py - An insecure password locker program

import sys, pyperclip

PASSWORDS = {'email'  : 'Temporaryemailfornow',
             'blog'   : 'blogemailfornow',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account ' + account)

'''I can use this at any point to copy generic sentences that would
    can be used to email out to people or for passwordsself.
    Maybe use this for generic thank you emails for interviewsself.
'''
