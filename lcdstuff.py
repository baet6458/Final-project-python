from RPLCD1.i2c import CharLCD
import time

#intialize the LCD
lcd = CharLCD('PCF8574', 0x27)
washerNumber = 0
dryerNumber = 0

def dispFirstScreen():
    lcd.clear()
    #setup first screen
    lcd.write_string('Available washers:' + str(washerNumber))
    lcd.cursor_pos = (1, 0)
    lcd.write_string('Available dryers:' + str(dryerNumber))
    lcd.cursor_pos = (3,0)
    lcd.write_string('Press A to continue')

def dispSecondScreen():
    lcd.clear()
    lcd.cursor_pos =(0,0)
    lcd.write_string('1.Clear a machine')
    lcd.cursor_pos = (1, 0)
    lcd.write_string('2.Message a user')
    lcd.cursor_pos = (2,0)
    lcd.write_string('3.Take a machine')
    lcd.cursor_pos = (3,0)
    lcd.write_string('Pick a number:')
    lcd._set_cursor_mode('blink')

def dispMachineinfo():
    lcd.clear()
    lcd._set_cursor_mode('blink')
    lcd.write_string('hi\b')

while(1):
    dispFirstScreen()
        
    while(input()!= 'A'):
        #do nothing
        dispFirstScreen()

    dispSecondScreen()
    reply=input()
    lcd.write_string(reply)

    while(reply != '1' and reply != '2' and reply != '3'):
        reply=input()
        if reply=='b':
            row ,col = lcd._cursor_pos
            if(col>14):
                    lcd.cursor_pos=(3, (col-1))
                    lcd.write_string("\b")
                    lcd.cursor_pos=(row,col-1)
        else:
            lcd.write_string(reply)

    if reply == '1':
        #clear a machine
        lcd.clear()
        lcd.write_string('Machine number:')
        reply=input()
        lcd.write_string(reply)
        while(reply!='d'):
            reply=input()
            if reply=='b':
                row ,col = lcd._cursor_pos
                print(col)
                if(col>14):
                    lcd.cursor_pos=(row, (col-1))
                    lcd.write_string("\b")
                    lcd.cursor_pos=(row,col-1)
            else:
                lcd.write_string(reply)
            if(reply!='d' and reply!='b'):
                machine=reply
        if(int(machine)>3):
            dryerNumber+=1
        else:
            washerNumber+=1
        lcd.clear()
        lcd.write_string('returning to menu')
        time.sleep(2)
        dispFirstScreen()
    elif reply== '2':
        #message a user
        lcd.clear()
        lcd.write_string('Machine number:')
    elif reply=='3':
        #take a machine
        lcd.clear()
        lcd.write_string('Bond number:')
