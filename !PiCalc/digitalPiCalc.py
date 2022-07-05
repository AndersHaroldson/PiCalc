# This is a digital version of PiCalc
# It does not include any Rpi imports
import math

def main():
    uin = input("Type some equation: ")
    print(eval(uin))
    
def strTest():
    str = " "
    for i in range(1, 10):
        new = str + "1"
        print(new)

strTest()

#main()