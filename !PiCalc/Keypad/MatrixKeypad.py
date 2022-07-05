#!/usr/bin/env python3
########################################################################
# Filename    : MatrixKeypad.py
# Description : obtain the key code of 4x4 Matrix Keypad
# Author      : freenove
# modification: 2018/08/03
########################################################################
import RPi.GPIO as GPIO
import Keypad       #import module Keypad
ROWS = 4        # number of rows of the Keypad
COLS = 4        #number of columns of the Keypad
keys = [    '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            '*', '0', '=', '/'  ]

rowsPins = [16, 20, 21, 5]
colsPins = [6, 13, 19, 26]

def loop():
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #creat Keypad object
    keypad.setDebounceTime(50)      #set the debounce time
    while(True):
        key = keypad.getKey()       #obtain the state of keys
        if(key != keypad.NULL):     #if there is key pressed, print its key code.
            print ("You Pressed Key : %c "%(key))
            
if __name__ == '__main__':     #Program start from here
    print ("Program is starting ... ")
    try:
        loop()
    except KeyboardInterrupt:  #When 'Ctrl+C' is pressed, exit the program. 
        GPIO.cleanup()
