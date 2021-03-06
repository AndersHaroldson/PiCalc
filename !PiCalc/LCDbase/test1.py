from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep

#uin = input("Enter your equation: ")

def loop():
    mcp.output(3, 1)     # turn on LCD backlight
    lcd.begin(16, 2)     # set number of LCD lines and columns
    while(True):
        #lcd.clear()
        lcd.setCursor(0, 0)
        lcd.message(str(eval(uin)))  
        #lcd.message()
        sleep(1)


def destroy():
    lcd.clear()


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
        loop()
    except KeyboardInterrupt:
        destroy()
