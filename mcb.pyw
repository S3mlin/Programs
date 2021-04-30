
#Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyboard
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#       py.exe mcb.pyw list - Loads all keywords to clipboard
#       py.exe mcb.pyw deleteall - Deletes all keywords
#       py.exe mcb.pyw delete <keyword> - Deletes keyword from clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #List keyword and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(mcbShelf[sys.argv[1]])
    #Delete all keywords
    elif sys.argv[1].lower() == 'deleteall':
        mcbShelf.clear()
#Delete a keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
mcbShelf.close()