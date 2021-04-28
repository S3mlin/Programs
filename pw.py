
#pw.py - Nesiguran program za spremanje sifra.

Sifre = {'email': 'kekmao7mail', 'facebook': 'rip3', 'blog': 'nista4'}

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # prva linija arg je ime accounta

if account in Sifre:
    pyperclip.copy(Sifre[account])
    print('Password for ' +account+ ' copied to clipboard.')
else:
    print('There is no account named '+account+'.')