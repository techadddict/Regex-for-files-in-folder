"""
The program opens all .txt files in a folder
and searches for any line that matches a user-supplied regular
expression. The results should be printed to the screen.

"""

import re
import os
import glob

def find_regex(word_pattern,path_to_folder):
    os.chdir(path_to_folder)
    for filename in glob.glob('*.txt'):
        file=open(filename,'r')
        lines =file.readlines()
        for line in lines:
            regex_find= re.compile(word_pattern)
            get_search=regex_find.findall(line)
            if(len(get_search)>0):
                print(get_search)
            else:
                print('No match found')
    return




os.mkdir('path')
os.chdir('path')
for i in range(1,10):
    new_file= open('./Text' +str(i)+'.txt','w')
    new_file.write('nd file paths. For instance, you’ve already used os.path.join() to build'+str(i)*4+ 'paths in a way that will work on any operating system. Since os.path is a module inside the os module, you can import it by simply running import os. Whenever your programs need to work with files, folders, or file paths, you can refer to the short examples in this section')
    new_file.write('Calling os.path.dirname(path) will return a string of everything that comes before the last slash in the path argument. Calling os.path.basename(path) will return a string of everything that comes after the last slash in the path argu- ment. The dir name and base name of a path are outlined in Figure8-4')
    new_file.write('Also, note698 that os.path.split() does not take a file path and return a list of strings of each folder. For that, use the split() string method and split on the string in os.sep. Recall478 from earlier that the os.sep variable is set to the correct folder-separating slash222 for the computer running the program.')
    new_file.close()


pattern='[a-z]+[0-9]+|[A-Z]+[a-z]+[0-9]+'
find_regex(pattern,'path')
