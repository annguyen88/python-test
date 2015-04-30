#!/usr/bin/python

def renamer():
    for iname in os.listdir('.'):
        first, second = iname.replace(" ", "").split("-")
        number, ext = second.split('.')
        first, number, ext = first.strip(), number.strip(), ext.strip()
        number = '0'*(6-len(number)) + number  # pad the number to be 7 digits long
        oname = first + "-" + number + '.' + ext
        os.rename(iname, oname)
    print "Done"
