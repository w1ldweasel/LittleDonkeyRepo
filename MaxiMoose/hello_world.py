# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a hello world file.
"""

#!/python

import platform

def main():
    print('\n')  
    print('Hello World!')
    name = input('What is your name? >')  
    print('\n')        
    print ('Hello ', name)
def message():
  print('This is python version {}'.format(platform.python_version()))

if __name__ == '__main__': main()
