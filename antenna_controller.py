
from Tkinter import *

master = Tk()

def create_control_button(text,row,column,command):
    button= Button(master, text=text,height=3,width=8,command=command)
    button.grid(row=row,column=column,rowspan=3,columnspan=3,padx=10, pady=10)
    return button

global auto
auto = False
font_size = 25

antenna_az=Label(text="0,0",font=font_size)
antenna_el=Label(text="0,0",font=font_size)
moon_az=Label(text="0,0",font=font_size)
moon_el=Label(text="0,0",font=font_size)

# Event-methods

def action_increment_az():
    global az
    
    print("action_increment_az")

def action_decrement_az():
    print("action_decrement_az")
    
def action_stop_motor():
    print("stop motor")

def action_increment_el():
    print("action_increment_el")

def action_decrement_el():
    print("action_decrement_el")
    
def action_clear_console():
    print("action_clear_console")

def action_quit_application():
    print("action_quit_application")

def action_auto():
    global auto
    if auto:
        indicate_manual_on()
        auto=False
    else:
        indicate_auto_on()
        auto=True

#Methods for changing the state

def indicate_auto_on():
    auto_vs_manual_button.config(background="green",text="set manual")
    
def indicate_manual_on():
    auto_vs_manual_button.config(background="orange",text="set auto")


def indicate_set_antenna(az,el):
    antenna_az.config(text=str(az))
    antenna_el.config(text=str(el))

def indicate_set_moon(az,el):
    moon_az.config(text=str(az))
    moon_el.config(text=str(el))

# Setting title
master.wm_title("Antenna controller")

# Control-segment
create_control_button("AZ +" ,row=1,column=3,command=action_increment_az)
create_control_button("STOP" ,row=4,column=3,command=action_stop_motor)
create_control_button("EL-"  ,row=4,column=1,command=action_increment_el)
create_control_button("EL+"  ,row=4,column=5,command=action_decrement_el)
create_control_button("AZ -" ,row=7,column=3,command=action_decrement_az)

# Console
create_control_button("Clear",row=10,column=0,command=action_clear_console)

text_console = Text(master, height=4,width=40)
text_console.grid(row=10,column=3,columnspan=3)

Label(text="UTC").grid(row=0,column=0)
Label(text="00:00:00").grid(row=0,column=1)

# Output-table
Label(text="AZ",font=font_size).grid(row=1,column=9)
Label(text="EL",font=font_size).grid(row=1,column=10)
 
Label(text="Antenna",font=font_size).grid(row=2,column=6,columnspan=3)
antenna_az.grid(row=2,column=9)  
antenna_el.grid(row=2,column=10)

Label(text="Moon",font=font_size).grid(row=3,column=6,columnspan=3)
moon_az.grid(row=3,column=9)  
moon_el.grid(row=3,column=10)

auto_vs_manual_button = create_control_button("auto",row=7,column=5,command=action_auto)
indicate_manual_on()

# Others
create_control_button("corr",row=7,column=9,command=action_quit_application)
create_control_button("quit",row=10,column=9,command=action_quit_application)

indicate_set_antenna(5,6)
indicate_set_moon(20.6,1.5)

mainloop()

