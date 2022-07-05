from PCF8574 import *
#from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
import RPi.GPIO as GPIO
import Keypad
from time import sleep

ROWS = 4 
COLS = 4  
keys = ['1', '2', '3', '+',
        '4', '5', '6', '-',
        '7', '8', '9', '*',
        'C', '0', '=', '/']

rowsPins = [16, 20, 21, 5]
colsPins = [6, 13, 19, 26]

def runLoop():
    mcp.output(3, 1)     # turn on LCD backlight
    lcd.begin(16, 2)     # set number of LCD lines and columns

    keypad = Keypad.Keypad(keys, rowsPins, colsPins, ROWS, COLS)  # creat Keypad object
    keypad.setDebounceTime(50)
    
    eqStr = ""
    while(True):
        key = keypad.getKey()

        #lcd.setCursor(0, 0)
        #lcd.message(key)
        if(key != keypad.NULL): 
            if key == "=":
                lcd.setCursor(1, 1)
                lcd.message("= " + str(eval(eqStr)))
                lcd.setCursor(0, 0)
                eqStr = ""
            
            elif key == "C":
                lcd.clear()
                lcd.setCursor(0, 0)
                eqStr = ""

            else:
                lcd.message("%c" % (key))
                eqStr = eqStr + key

        sleep(0.1)


PCF8574_address = 0x27 
PCF8574A_address = 0x3F  

try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        runLoop()
    except KeyboardInterrupt:
        lcd.clear()
