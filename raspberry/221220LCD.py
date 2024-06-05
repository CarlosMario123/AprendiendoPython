from time import sleep
import I2C_LCD_driver


name = {
    "221220": ["Carlos Mario","Ruiz Pinacho"],
    "223184":["daniel","jesus","hernadez","gomez"],
    "223249":["ary coranado","avedaño"],
    "223231":["vinicio","alejeandro","portela","esquinca"]
    }

sleep(3)


milcd = I2C_LCD_driver.lcd()

#intregrantes
for matri in name:
    milcd.lcd_display_string(matri,2)
    for i in name[matri]:
        milcd.lcd_display_string(i,1)
        sleep(2)
        
