# Light_Gui
Working idea for a GUI to control tiny-tuya lights
I was inspired by this project https://github.com/jasonacox/tinytuya and
I was inspired by this project https://github.com/dev-est/tuya_tray  However I could never get it to work.(depeendeny issue)

So I started by testing some demo code and made this.

To made Lights_gui_5.ui intp py code used pyuic5 -o Lights_gui_5.py -x Lights_gui_5.ui

I dont know how to implement all my ideas.


** TODO  **

1 Get list and status of lights from the tyny-tuya module.  ----- done ish 
2 Make code respod to light name from decodeing JSON file.  ----- done ish 
3 Populate gui with all online lights status's
4 Add a title to the gui and make it a type of tray icon for ubuntu  ----- done ish 
5 keep it compatible with the android app called smartlife so tcp connection cannot be left open. ----- done ish 
6 Add a lock the two sliders togeter tickbox to gui

** Update **

On line 85, I cannot to get slider to update in GUI.
If I put a number instead of br_counter it works.
If I put self.Br_Slide.setValue(br_counter) the slider stays put. ---- Fixed 

Ive managed to make the gui and the other supporting code work as I wanted.

It can turn off all lights. Change colour temp and brightness.
I cannot get status to fill in the correct values for the slider. --- fixed


