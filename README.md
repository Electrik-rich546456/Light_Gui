# Light_Gui
Working idea for a GUI to control tiny-tuya lights

I was inspired by this project https://github.com/dev-est/tuya_tray  However I could never get it to work.

So I started by testing some demo code lights2.py

Then made Lights_gui_5.ui and used pyuic5 -o Lights_gui_5.py -x Lights_gui_5.ui to start my own but I do not know how to implement my ideas

** TODO  **

get list and status of lights using the tyny-tuya module decode JSON. module found here https://github.com/jasonacox/tinytuya
populate gui with all online lights status's

add a title to the gui and make it a type of tray icon for ubuntu 
keep it compatible with the android app called smartlife so tcp connection cannot be left open.
