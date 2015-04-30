# os is a library that gives us the ability to make OS changes
import os
 
def increment_file_numbers(directory, number):
        # iterate over every file name in the directory
        print directory
        for file_name in os.listdir(directory):
 
                # we know that first two characters are numbers
                print file_name
                file_number = int(file_name[0:2])
 
                # we only increment the files that are bigger than number
                if file_number > number:
                        new_file_number = file_number + 1
 
                        # use string formatting to pad single-digit nums w/ a 0
                        new_file_name = '%s/%02d%s' % (directory, new_file_number, file_name[2:])
                        old_file_name = '%s/%s' % (directory, file_name)
 
                        # rename the file!
                        os.rename(old_file_name, new_file_name)
 
# This is the path to these videos on my computer
PATH = os.path.abspath('/Users/anguyen/Github/python/test')
 
# Let's increment all the files w/ numbers above 11
increment_file_numbers(PATH, 1)


