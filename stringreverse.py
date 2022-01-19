#! /usr/bin/env python3
'''
stringreverse v0.1 - Copyright 2022 James Slaughter,
This file is part of stringreverse v0.1.

stringreverse v0.1 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

stringreverse v0.1 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with stringreverse v0.1.  If not, see <http://www.gnu.org/licenses/>. 
'''

#python import
import sys
import os
#import base64
#import binascii
#import struct
#import numpy as np
#from array import *
#from termcolor import colored

#programmer generated imports
from controller import controller

'''
Usage()
Function: Display the usage parameters when called
'''
def Usage():
    print ('stringreverse.py - Flip and reverse strings in a file.')
    print ('Usage: [required] --file [optional] --debug --help')
    print ('Example: ./stringreverse.py --file yourfile.123 --debug')
    print ('Required Arguments:')
    print ('--file - File being opened.')
    print ('Optional Arguments:')
    print ('--output - output file name of the new executable.  Will be output.exe by default otherwise.')
    print ('--debug - Prints verbose logging to the screen to troubleshoot issues with a recon installation.')
    print ('--help - You\'re looking at it!')
    sys.exit(-1)
            
'''
Parse() - Parses program arguments
'''
def Parse(args):        
    option = ''

    print ('[*] Length Arguments: ' + str(len(args)))

    if (len(args) == 1):
        return -1

    print ('[*] Arguments: ')
    for i in range(len(args)):
        if args[i].startswith('--'):
            option = args[i][2:]
                
            if option == 'help':
                return -1

            if option == 'file':
                CON.file = args[i+1]
                print (option + ': ' + CON.file)   

            if option == 'output':
                CON.output = args[i+1]
                print (option + ': ' + CON.output)                        
                
            if option == 'debug':
                CON.debug = True
                print (option + ': ' + str(CON.debug))

    if (len(CON.output) < 3):
        CON.output = 'output.exe' 

    print ('')   
    
    return 0

'''
Execute()
Function: - Does the doing
'''
def Execute():    
 
    write_file = ''

    try:
        print ('[-] Opening write file: ' + CON.output + '...')
        write_file = open(CON.output, 'wb')
    except Exception as e:
        print ('[x] Unable to open write file: ' + str(e))
        return -1

    print ('[-] Opening file to read: ' + CON.file + '...')
    for line in reversed(list(open(CON.file, 'rb'))):
        if (CON.debug == True):
            print('[-] Unreversed string: ' + str(line.rstrip()))
        if (CON.debug == True):
            print ('[-] Reversed string: ' + str(line[::-1]))

        write_file.write(line[::-1])

    write_file.close()
    print ('[*] Write Complete!')    
 
    return 0


'''
Terminate()
Function: - Attempts to exit the program cleanly when called  
'''
     
def Terminate(exitcode):
    sys.exit(exitcode)

'''
This is the mainline section of the program and makes calls to the 
various other sections of the code
'''

if __name__ == '__main__':
    
    ret = 0

    #Stores our args
    CON = controller()
                   
    #Parses our args
    ret = Parse(sys.argv)

    #Something bad happened
    if (ret == -1):
        Usage()
        Terminate(ret)

    #Do the doing
    print ('[*] Executing...')
    Execute()

    print ('')
    print ('[*] Program Complete!')

    Terminate(0)
'''
END OF LINE
'''

