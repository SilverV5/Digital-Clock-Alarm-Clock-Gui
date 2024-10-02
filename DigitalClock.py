import tkinter as tk
from datetime import datetime
import pygame

pygame.mixer.init()
is_muted = False
On = True

#loads music which inf plays 
pygame.mixer.music.load('tick.mp3')
pygame.mixer.music.play(-1)




#Deletes all packs and loads in new input spot for alarm clock
def alarm():
    global ask, set_time , info, submit_button, Alarm_clock
    Mute.pack_forget()
    Unmute.pack_forget()
    Alarm.pack_forget()
    Clock.pack_forget()
    pygame.mixer.music.pause()
    
    
    info = tk.Label(text="Please Input Time For Alarm:(HH:MM:SS AM/PM)")
    ask = tk.Entry()


    submit_button = tk.Button(text="Set Alarm", command=alarm_confirm)
    
    info.pack()
    ask.pack()
    submit_button.pack()
    Alarm_clock = tk.Label()
    Alarm_clock.pack()
    

def alarm_confirm():
    global ask, set_time, submit_button, Alarm_clock
    alarm_time = ask.get()
    if 'set_time' not in globals() or set_time is None:
        set_time= tk.Label()
        set_time.pack()
    try:
        alarm_time_strip = datetime.strptime(alarm_time, "%I:%M:%S %p").time()
        set_time.config(text=f'Alarm Has Been Set For: {alarm_time_strip}')
        info.pack_forget()
        ask.pack_forget()
        submit_button.pack_forget()
        
        check_alarm(alarm_time_strip)

    except ValueError:
        set_time.config(text="Invalid time format. Please use HH:MM:SS AM/PM.")
        
        
def check_alarm(alarm_time_strip):
    global Alarm_clock
    now = datetime.now()
    current_time = now.time()
    
    
    if current_time >= alarm_time_strip:
        pygame.mixer.music.pause()  # Pause the music
        text = tk.Label(text='Time Is Up!')
        text.pack()
        pygame.mixer.music.load('lingling.mp3')
        pygame.mixer.music.play()
        return  # Stop checking if the alarm has gone off
    else:
        # If the alarm time has not been reached, continue to check
        Alarm_clock.config(text=f"Current Time: {now.strftime('%I:%M:%S %p')}")
        Alarm_clock.after(1000, lambda: check_alarm(alarm_time_strip))  # Check again after 1 second
        

       



#this over here is the sigma time updater 
def time_update():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    Clock.config(text=current_time)
    Clock.after(1000, time_update)


#as the function name states mutes 
def mute():
    global On 
    pygame.mixer.music.pause() 
    On = False 

#unmutes like a sigma champ    
def unmute():
    global On
    pygame.mixer.music.unpause() 
    On = True


#this is the screen and title
window = tk.Tk()
window.title("Digital Clock")  
#this is the time shown pack function displays it
Clock = tk.Label(fg='green', bg='black')
Clock.pack()

#calls for time to update each second
time_update()

#mute button
Mute = tk.Button(
    text=" Mute!",
    width=5,
    height=1,
    bg="White",
    fg="Black",
    command=mute
)
#unmute button
Unmute = tk.Button(
    text="Unmute!",
    width=5,
    height=1,
    bg="White",
    fg="Black",
    command=unmute
)

#Alarm Clock
Alarm = tk.Button(
    text="Alarm!",
    width=5,
    height=1,
    bg="White",
    fg="Black",
    command=alarm

)



#loads the buttons
Mute.pack()
Unmute.pack()
Alarm.pack()






#this is used for the display to stay up i think
window.mainloop()